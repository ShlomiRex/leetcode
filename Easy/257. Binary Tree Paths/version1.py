# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    lst = []
    helper(root, "", lst)
    return lst

def helper(root: Optional[TreeNode], curr_path: str, lst: List[str]):
    if root:
        curr_path += "->"+str(root.val)
        # If Leaf we reached end of possible path
        if not root.left and not root.right:
            lst.append(curr_path[2:]) # Remove the first '->'
        else:
            helper(root.left, curr_path, lst)
            helper(root.right, curr_path, lst)

if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(3))
    res = binaryTreePaths(tree)
    assert "1->2->5" in res
    assert "1->3" in res
    
    tree = TreeNode(1)
    res= binaryTreePaths(tree)
    assert "1" in res

    tree = TreeNode(1, TreeNode(2))
    res = binaryTreePaths(tree)
    assert "1->2" in res
    