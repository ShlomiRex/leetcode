from typing import Optional

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
            self.helper(root)
            return self.res
        return 0

    def helper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        l_without_split = self.helper(root.left)
        r_without_split = self.helper(root.right)

        # We can either take the left path, right path, or none of them, for current node
        leftPathMaxSum = max(l_without_split, 0)
        rightPathMaxSum = max(r_without_split, 0)

        # If we split
        self.res = max(self.res, root.val + leftPathMaxSum + rightPathMaxSum)

        return root.val + max(leftPathMaxSum, rightPathMaxSum)


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

    # Failed on test 77/95
    tree = TreeNode(1, TreeNode(-2), TreeNode(3))
    res = Solution().maxPathSum(tree)
    print(res)
    assert res == 4