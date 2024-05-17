"""
Runtime: 41 ms beats 82%
Memory: 17.12 MB beats 28%
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def removeLeafNodes(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    if root is None:
        return None
    root.left = removeLeafNodes(root.left, target)
    root.right = removeLeafNodes(root.right, target)
    if root.left is None and root.right is None and root.val == target:
        return None
    return root

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(3, TreeNode(2), TreeNode(4)))
    res = removeLeafNodes(root, 2)
    assert res.val == 1
    assert res.right.val == 3
    assert res.left == None
    assert res.right.right.val == 4
    assert res.right.left == None
    
    root = TreeNode(1, TreeNode(3, TreeNode(3), TreeNode(2)), TreeNode(3))
    res = removeLeafNodes(root, 3)
    assert res.val == 1
    assert res.right == None
    assert res.left.val == 3
    assert res.left.left == None
    assert res.left.right.val == 2
    
    root = TreeNode(1, TreeNode(2, TreeNode(2, TreeNode(2))))
    res = removeLeafNodes(root, 2)
    assert root.val == 1
    assert root.left == None
    assert root.right == None