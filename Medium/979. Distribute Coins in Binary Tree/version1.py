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
    # For each node check leftSum, rightSum, leftCount, rightCount
    # def dfs1(curr, level):
    #     if curr is None:
    #         return 0, 0
    #     leftSum, leftCount = dfs1(curr.left, level+1)
    #     rightSum, rightCount = dfs1(curr.right, level+1)

    #     a,b = leftSum+rightSum+curr.val, leftCount+rightCount+1
    #     curr.val = (curr.val, leftSum, rightSum, leftCount, rightCount, level)
    #     return a,b
    
    ans = [0]
    # Propogate upwards from leafs to root
    def dfs2(curr):
        if curr is None:
            return 0
        
        # # If leaf
        # if curr.left is None and curr.right is None:
        #     # Check what we can spare upwards
        #     if curr.val == 1:
        #         return 0 # We can't spare anything
        #     elif curr.val == 0:
        #         ans[0] += 1
        #         return -1 # We need 1 coin
        #     else:
        #         return curr.val-1 # curr.val > 1 we can spare all the coins except 1.
        
        # Not leaf - decide what to do with return values of left, right subtree
        
        leftSpare = dfs2(curr.left)
        rightSpare = dfs2(curr.right)

        totalSpare = leftSpare + rightSpare + curr.val

        # Take one coin for yourself
        totalSpare -= 1

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
            
        
    #dfs1(root, 0)
    rootSpare = dfs2(root)
    return ans[0]

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(0), TreeNode(0))
    assert distributeCoins(root) == 2

    root = TreeNode(0, TreeNode(3), TreeNode(0))
    assert distributeCoins(root) == 3