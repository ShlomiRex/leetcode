"""
Runtime: 38 ms beats 40%
Memory: 16.5 MB beats 26%

Instead of returning None we return the sum 0, since we check if we returned None then leftSum is 0 anyways.
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root: Optional[TreeNode]) -> int:
    def sumPath(head, curr_path) -> int:
        if not head:
            return 0
        
        # Append to curr path
        curr_path.append(head.val)

        # If leaf, we can return path
        if head.left is None and head.right is None:
            return int(''.join(str(x) for x in curr_path))
        
        # Recursivly call with deep copy of the curr_path
        leftSum = sumPath(head.left, curr_path[:])
        rightSum = sumPath(head.right, curr_path[:])

        return leftSum + rightSum
    
    return sumPath(root, [])

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sumNumbers(root) == 25

    root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    assert sumNumbers(root) == 1026

    root = TreeNode(0, TreeNode(1))
    assert sumNumbers(root) == 1

    root = TreeNode(1, TreeNode(0))
    assert sumNumbers(root) == 10