"""
Runtime: 34 ms beats 67%
Memory: 16.5 MB beats 34%
Time taken: 2 minutes 36 seconds
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    leftSubtree = invertTree(root.left)
    rightSubtree = invertTree(root.right)
    root.left = rightSubtree
    root.right = leftSubtree
    return root

if __name__ == "__main__":
    left = TreeNode(2, TreeNode(1), TreeNode(3))
    right = TreeNode(7, TreeNode(6), TreeNode(9))
    root = TreeNode(4, left, right)
    ans = invertTree(root)
    assert ans.val == 4
    assert ans.left.val == 7
    assert ans.right.val == 2
    
    assert ans.left.left.val == 9
    assert ans.left.right.val == 6

    assert ans.right.left.val == 3
    assert ans.right.right.val == 1