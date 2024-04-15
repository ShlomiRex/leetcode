from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(curr_node, curr_sum):
        if curr_node is None:
            return False
        curr_sum += curr_node.val
        if curr_sum == targetSum and curr_node.left is None and curr_node.right is None:
            return True
        return dfs(curr_node.left, curr_sum) or dfs(curr_node.right, curr_sum)
    return dfs(root, 0)