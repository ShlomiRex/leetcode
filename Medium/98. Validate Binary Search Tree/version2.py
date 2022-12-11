# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:
	if root == None:
		return True
	if isValidBSTHelper(root.left, float("-inf"), root.val) == False:
		return False
	if isValidBSTHelper(root.right, root.val, float("inf")) == False:
		return False
	return True

def isValidBSTHelper(root: Optional[TreeNode], left_range, right_range) -> bool:
	if root == None:
		return True
	if root.val >= right_range or root.val <= left_range:
		return False
	if isValidBSTHelper(root.left, left_range, root.val) == False:
		return False
	if isValidBSTHelper(root.right, root.val, right_range) == False:
		return False
	return True
	

if __name__ == "__main__":
	root = TreeNode(2, TreeNode(1), TreeNode(3))
	assert isValidBST(root) == True
	
	right = TreeNode(4, TreeNode(3), TreeNode(6))
	root = TreeNode(5, TreeNode(1), right)
	assert isValidBST(root) == False

	root = TreeNode(5)
	assert isValidBST(root) == True

	root = TreeNode(5, left = TreeNode(6))
	assert isValidBST(root) == False

	root = None
	assert isValidBST(root) == True