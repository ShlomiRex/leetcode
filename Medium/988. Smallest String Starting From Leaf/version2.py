"""
Runtime: 42 ms beats 66%
Memory: 17.7 MB beats 53%

Instead of storing all the strings in array and then sorting it, we can use a single minimum string variable that we change when we find minimum lexicographically string.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
def smallestFromLeaf(root: Optional[TreeNode]) -> str:
    ans = [None]
    def dfs(curr, stack):
        if not curr:
            return
        
        # Convert numbers 0-25 to characters 'a' - 'z'
        stack.append(chr(ord('a') + curr.val))

        # If leaf we got to final string character
        if curr.left is None and curr.right is None:
            str_path = ''.join(stack[::-1]) # Reverse and create string
            ans[0] = str_path if ans[0] is None else min(ans[0], str_path)
            return
        # Recursivly call DFS with deep copy of stack
        dfs(curr.left, stack[:])
        dfs(curr.right, stack[:])
    dfs(root, [])
    return ans[0]

if __name__ == "__main__":
    left = TreeNode(1, TreeNode(3), TreeNode(4))
    right = TreeNode(2, TreeNode(3), TreeNode(4))
    root = TreeNode(0, left, right)
    assert smallestFromLeaf(root) == "dba"