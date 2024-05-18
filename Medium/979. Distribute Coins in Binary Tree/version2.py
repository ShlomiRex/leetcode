"""
Runtime: 26 ms beats 98%
Memory: 16.5 MB beats 90%
Time taken: 1 hour 12 minutes

I'm so proud that I successfully did this question after 1 hour WITHOUT looking at hints or solutions
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def distributeCoins(root: Optional[TreeNode]) -> int:
    ans = [0]
    # Propogate upwards from leafs to root
    def dfs(curr):
        if curr is None:
            return 0
        
        # Not leaf - decide what to do with return values of left, right subtree
        leftSpare = dfs(curr.left)
        rightSpare = dfs(curr.right)

        # Take one coin for yourself (-1 at the end)
        totalSpare = leftSpare + rightSpare + curr.val - 1

        if totalSpare > 0:
            # Now we can use totalSpare
            # We move 'totalSpare' coins upwards, so we increase ans by that amount
            ans[0] += totalSpare
            return totalSpare
        elif totalSpare < 0:
            # We need to get more coins!
            ans[0] += (-totalSpare)
            return totalSpare
        else:
            # We have no spare, we don't move any coins
            return totalSpare
            
    dfs(root)
    return ans[0]

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(0), TreeNode(0))
    assert distributeCoins(root) == 2

    root = TreeNode(0, TreeNode(3), TreeNode(0))
    assert distributeCoins(root) == 3