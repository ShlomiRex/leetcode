"""
Runtime: 40 ms beats 90%
Memory: 17.6 MB beats 97%
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    def dfs(curr_node, curr_depth):
        if curr_node is None or curr_depth >= depth: return
        if curr_depth == depth - 1:
            curr_node.left, curr_node.right  = TreeNode(val, left=curr_node.left), TreeNode(val, right=curr_node.right)
            return
        dfs(curr_node.left, curr_depth+1)
        dfs(curr_node.right, curr_depth+1)
    if depth != 1:
        dfs(root, 1)
    else:
        root = TreeNode(val, left=root)
    return root

if __name__ == "__main__":
    left = TreeNode(2, TreeNode(3), TreeNode(1))
    right = TreeNode(6, TreeNode(5))
    root = TreeNode(4, left, right)
    res = addOneRow(root, 1, 2)

    assert res.val == 4
    assert res.left.val == 1
    assert res.right.val == 1
    assert res.left.left.val == 2
    assert res.right.right.val == 6
    
    left = TreeNode(2, TreeNode(3), TreeNode(1))
    root = TreeNode(4, left)
    res = addOneRow(root, 1, 3)

    assert res.val == 4
    assert res.left.val == 2
    assert res.left.left.val == 1
    assert res.left.right.val == 1
    assert res.left.left.left.val == 3
    assert res.left.right.right.val == 1