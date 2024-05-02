"""
Runtime: 35 ms beats 54%
Memory: 16.4 MB beats 96%
Time taken: 3 minutes 56 seconds
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def dfs(rootA, rootB):
        if rootA is None and rootB is None:
            return True
        if rootA and rootB and rootA.val == rootB.val:
            return dfs(rootA.left, rootB.left) and dfs(rootA.right, rootB.right)
        return False
    return dfs(p, q)

if __name__ == "__main__":
    rootA = TreeNode(1, TreeNode(2), TreeNode(3))
    rootB = TreeNode(1, TreeNode(2), TreeNode(3))
    assert isSameTree(rootA, rootB) == True

    rootA = TreeNode(1, TreeNode(2))
    rootB = TreeNode(1, None, TreeNode(3))
    assert isSameTree(rootA, rootB) == False

    rootA = TreeNode(1, TreeNode(2), TreeNode(1))
    rootB = TreeNode(1, TreeNode(1), TreeNode(2))
    assert isSameTree(rootA, rootB) == False