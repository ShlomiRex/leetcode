"""
Runtime: 37 ms beats 46%
Memory: 16.6 MB beats 26%

Approach: keep track of current path: [1,2,3]. If we reached leaf, we convert curr_path (array of integers)
to string and then to single integer, and we return this path sum.
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
            return
        
        # Append to curr path
        curr_path.append(head.val)

        # If leaf, we can return path
        if head.left is None and head.right is None:
            return int(''.join(str(x) for x in curr_path))
        
        # Recursivly call with deep copy of the curr_path
        leftSum = sumPath(head.left, curr_path[:])
        rightSum = sumPath(head.right, curr_path[:])

        # Deal with None returned from 
        leftSum = leftSum if leftSum else 0
        rightSum = rightSum if rightSum else 0

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