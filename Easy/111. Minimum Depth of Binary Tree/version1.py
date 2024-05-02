"""
Runtime: 298 ms beats 13%
Memory: 43 MB beats 34%
Time taken: 7 minutes 36 seconds
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
    def dfs(root, curr_height, curr_min_depth):
        if root is None:
            return curr_min_depth
        if root.left is None and root.right is None: # Leaf
            curr_min_depth = min(curr_min_depth, curr_height)
            return curr_min_depth
        leftMin = dfs(root.left, curr_height+1, curr_min_depth)
        rightMin = dfs(root.right, curr_height+1, curr_min_depth)
        return min(leftMin, rightMin)
    
    return dfs(root, 1, float('inf'))

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert minDepth(root) == 2

    root = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
    assert minDepth(root) == 5