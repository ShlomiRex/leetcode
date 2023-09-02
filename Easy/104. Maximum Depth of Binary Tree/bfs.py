# BFS Implementation

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.queue = []

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        self.queue.append(root)
        while self.queue:
            for i in range(len(self.queue)):
                node = self.queue.pop(0)
                if node.left:
                    self.queue.append(node.left)
                if node.right:
                    self.queue.append(node.right)
            level += 1
        return level


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

    root = TreeNode(1)  # lvl 1
    root.left = TreeNode(2)  # lvl 2
    root.right = TreeNode(5)  # lvl 2
    root.left.right = TreeNode(3)  # lvl 3
    root.left.right.left = TreeNode(1)  # lvl 4
    assert Solution().maxDepth(root) == 4
