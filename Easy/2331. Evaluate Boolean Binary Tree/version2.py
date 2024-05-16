"""
Runtime: 46 ms beats 63%
Memory: 16.86 MB beats 50%
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def evaluateTree(root: Optional[TreeNode]) -> bool:
    if root.val in [0, 1]: return root.val
    left, right = evaluateTree(root.left), evaluateTree(root.right)
    return (left or right) if root.val == 2 else (left and right)

if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
    assert evaluateTree(root) == True

    root = TreeNode(0)
    assert evaluateTree(root) == False