# This solution is 2ms slower than version 1.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.paths = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.helper(root, "")
        return self.paths

    def helper(self, root: Optional[TreeNode], curr_path: str):
        if root:
            curr_path += "->"+str(root.val)
            if not root.left and not root.right:
                self.paths.append(curr_path[2:])
            else:
                self.helper(root.left, curr_path)
                self.helper(root.right, curr_path)

if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(3))
    
    res = Solution().binaryTreePaths(tree)
    assert "1->2->5" in res
    assert "1->3" in res
    
    tree = TreeNode(1)
    res= Solution().binaryTreePaths(tree)
    assert "1" in res

    tree = TreeNode(1, TreeNode(2))
    res = Solution().binaryTreePaths(tree)
    assert "1->2" in res
    