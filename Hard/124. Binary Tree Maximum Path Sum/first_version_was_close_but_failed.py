from typing import Optional

# This is my original answer, it passed 52/95 tests. I couldn't fix it so I looked at other answers. It was really close.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def __init__(self):
        self.res = 0
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root:
            self.res = root.val
            return self.helper(root)
        return 0

    def helper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left or root.right:
            l_without_split = self.maxPathSum(root.left)
            r_without_split = self.maxPathSum(root.right)
            # If we split
            self.res = max(self.res, root.val + l_without_split + r_without_split)
            # If we don't split
            self.res = max(self.res, root.val + l_without_split)
            self.res = max(self.res, root.val + r_without_split)
        return self.res

if __name__ == "__main__":
    tree = TreeNode(1)
    assert Solution().maxPathSum(tree) == 1

    tree = TreeNode(1, TreeNode(2))
    res = Solution().maxPathSum(tree)
    print(res)
    assert res == 3

    tree = TreeNode(1, left=None, right=TreeNode(2))
    assert Solution().maxPathSum(tree) == 3

    tree = TreeNode(1, TreeNode(2), TreeNode(3))
    assert Solution().maxPathSum(tree) == 6

    tree = TreeNode(1, TreeNode(3), TreeNode(2))
    res = Solution().maxPathSum(tree)
    print(res)
    assert res == 6

    tree = TreeNode(1, TreeNode(2), TreeNode(3, right=TreeNode(4)))
    assert Solution().maxPathSum(tree) == 10
    
    tree = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().maxPathSum(tree) == 42

    # Failed on test 40/95... root is minus 3. self.res = 0 at the start.
    tree = TreeNode(-3)
    assert Solution().maxPathSum(tree) == -3

    tree = TreeNode(-3, TreeNode(-5))
    assert Solution().maxPathSum(tree) == -3

    # After fixing test 40/95 I failed on test 42/95
    tree = TreeNode(-2, TreeNode(1))
    assert Solution().maxPathSum(tree) == 1

    tree = TreeNode(1, TreeNode(-2))
    assert Solution().maxPathSum(tree) == 1

    # I failed on test 50/95
    tree = TreeNode(2, TreeNode(-1), TreeNode(-2))
    res = Solution().maxPathSum(tree)
    print(res)
    assert res == 2