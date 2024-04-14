"""
Runtime: 39 ms beats 36%
Memory: 16.7 MB beats 47%
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    def dfs(root, is_left) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None: # We reached leaf
            if is_left:
                return root.val
            return 0
        left_subtree_sum = dfs(root.left, True)
        right_subtree_sum = dfs(root.right, False)
        return left_subtree_sum + right_subtree_sum
    return dfs(root, False)
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sumOfLeftLeaves(root) == 24

    root = TreeNode(1)
    assert sumOfLeftLeaves(root) == 0