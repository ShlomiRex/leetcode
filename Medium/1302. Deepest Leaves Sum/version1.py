"""
Runtime: 146 ms beats 8%
Memory: 19 MB beats 88%
Time taken: 12 minutes 46 seconds

First intuition:

1. Find which subtree has deepest leaves
2. Calculate sum of that subtree

We can calculate sum while traversing the tree, and also counting how many nodes/leafs we have at the same time in one traversal.

After read the example:
I need to find the deepest level of the tree.
Only then, I sum all the nodes of that level. In the first example: 7+8=15

How:
DFS - Go to leafs first
If leaf, store level and sum

Maybe hashmap - key is level number, value is sum of that level?
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    lvl_sum_hashmap = {}
    deepest_level = [0] # We guarenteed number of nodes >= 1
    def dfs(root, curr_level):
        if root is None:
            return
        deepest_level[0] = max(deepest_level[0], curr_level)
        if curr_level not in lvl_sum_hashmap:
            lvl_sum_hashmap[curr_level] = 0
        lvl_sum_hashmap[curr_level] += root.val
        dfs(root.left, curr_level+1)
        dfs(root.right, curr_level+1)
    dfs(root, 0)
    return lvl_sum_hashmap[deepest_level[0]]

if __name__ == "__main__":
    l = TreeNode(2, TreeNode(4, TreeNode(7), None), TreeNode(5))
    r = TreeNode(3, None, TreeNode(6, None, TreeNode(8)))
    root = TreeNode(1, l, r)
    assert deepestLeavesSum(root) == 15
