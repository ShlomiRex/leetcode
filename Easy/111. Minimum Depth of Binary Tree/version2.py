"""
Runtime: 357 ms beats 5% (worse)
Memory: 43.5 MB beats 27% (worse)
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def minDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    leftMin, rightMin = float('inf'), float('inf')
    if root.left:
        leftMin = minDepth(root.left)
    if root.right:
        rightMin = minDepth(root.right)
    return min(leftMin, rightMin) + 1

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert minDepth(root) == 2

    root = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
    assert minDepth(root) == 5