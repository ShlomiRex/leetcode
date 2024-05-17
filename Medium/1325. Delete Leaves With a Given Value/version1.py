"""
Runtime: 56 ms beats 6%
Memory: 17.1 MB beats 80%
Time taken: 8 minutes 12 seconds
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def removeLeafNodes(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    # DFS until we reach leafs
    def dfs(curr, parent):
        if curr is None:
            return

        dfs(curr.left, curr)
        dfs(curr.right, curr)

        # Delete leaf node
        if curr.left is None and curr.right is None and curr.val == target:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
        
    dfs(root.left, root)
    dfs(root.right, root)
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