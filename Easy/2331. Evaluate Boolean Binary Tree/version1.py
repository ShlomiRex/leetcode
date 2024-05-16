"""
Runtime: 39 ms beats 92%
Memory: 16.88 MB beats 49.94%
Time taken: 4 minutes 49 seconds
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def evaluateTree(root: Optional[TreeNode]) -> bool:
    if root.val in [0, 1]:
        return root.val
    
    left = evaluateTree(root.left)
    right = evaluateTree(root.right)

    if root.val == 2: # OR
        return left or right
    elif root.val == 3: # AND
        return left and right
    else:
        print("ERROR: VAL: ", root.val)

if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
    assert evaluateTree(root) == True

    root = TreeNode(0)
    assert evaluateTree(root) == False