"""
Runtime: 40 ms beats 76%
Memory: 18 MB beats 17%
Time taken: probably 10-15 minutes, the intuition took me some time since I didn't know what is 'lexicographically smaller'.
First intution: traverse entire tree, put strings in dictionary. After traversal, sort strings. Return smallest string lexicographically (first element).
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
def smallestFromLeaf(root: Optional[TreeNode]) -> str:
    strings = []
    def dfs(curr, stack):
        if not curr:
            return
        
        # Convert numbers 0-25 to characters 'a' - 'z'
        stack.append(chr(ord('a') + curr.val))

        # If leaf we got to final string character
        if curr.left is None and curr.right is None:
            stack.reverse()
            strings.append(''.join(stack))
            return

        # Recursivly call DFS with deep copy of stack
        dfs(curr.left, stack[:])
        dfs(curr.right, stack[:])
    dfs(root, [])
    strings.sort()
    return strings[0]

if __name__ == "__main__":
    left = TreeNode(1, TreeNode(3), TreeNode(4))
    right = TreeNode(2, TreeNode(3), TreeNode(4))
    root = TreeNode(0, left, right)
    assert smallestFromLeaf(root) == "dba"