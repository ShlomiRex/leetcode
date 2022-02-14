from typing import Optional

"""
Runtime: 69 ms, faster than 26.75% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.3 MB, less than 18.15% of Python3 online submissions for Maximum Depth of Binary Tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # Calculate max depth of left sub tree
        left_max_depth = self.maxDepth(root.left)
        # Calculate max depth of right sub tree
        right_max_depth = self.maxDepth(root.right)

        return max(left_max_depth, right_max_depth) + 1  # We consider the rot node


if __name__ == "__main__":
    root = TreeNode(1)
    assert Solution().maxDepth(root) == 1

    root = TreeNode(1)
    root.left = TreeNode(2)
    assert Solution().maxDepth(root) == 2

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert Solution().maxDepth(root) == 3

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(5)
    assert Solution().maxDepth(root) == 3

    root = TreeNode(1) # lvl 1
    root.left = TreeNode(2) # lvl 2
    root.right = TreeNode(5) # lvl 2
    root.left.right = TreeNode(3) # lvl 3
    root.left.right.left = TreeNode(1)  # lvl 4
    assert Solution().maxDepth(root) == 4
