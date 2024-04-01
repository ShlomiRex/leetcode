"""
Runtime: 117 ms beats 43%
Memory: 19 MB beats 98%

Actually we don't need hashmap to store sum of all nodes of that level.
Only a single integer that represents the sum, and another integer that represents the deepest level.
We can update the sum and deepest level while traversing the tree.
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    deepest_lvl_sum = [0]
    deepest_lvl = [0] # We guarenteed number of nodes >= 1
    def dfs(root, curr_level):
        if root is None:
            return
        if curr_level == deepest_lvl[0]:
            deepest_lvl_sum[0] += root.val
        elif curr_level > deepest_lvl[0]:
            deepest_lvl_sum[0] = root.val
            deepest_lvl[0] = curr_level
        dfs(root.left, curr_level+1)
        dfs(root.right, curr_level+1)
    dfs(root, 0)
    return deepest_lvl_sum[0]

if __name__ == "__main__":
    l = TreeNode(2, TreeNode(4, TreeNode(7), None), TreeNode(5))
    r = TreeNode(3, None, TreeNode(6, None, TreeNode(8)))
    root = TreeNode(1, l, r)
    assert deepestLeavesSum(root) == 15
