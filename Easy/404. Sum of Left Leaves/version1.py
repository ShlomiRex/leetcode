"""
Runtime: 46 ms beats 7.5%
Memory: 16.6 MB beats 93%
Time taken: 3 minutes !
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    ans = [0]
    def dfs(root):
        if root is None:
            return False
        if root.left == None and root.right == None: # We reached leaf
            return True
        if dfs(root.left):
            ans[0] += root.left.val
        dfs(root.right)
        return False
    dfs(root)
    return ans[0]
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sumOfLeftLeaves(root) == 24

    root = TreeNode(1)
    assert sumOfLeftLeaves(root) == 0