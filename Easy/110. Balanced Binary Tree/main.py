from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:
	isBalanced, _ = isBalancedHelper(root)
	return isBalanced

def isBalancedHelper(root: Optional[TreeNode]) -> Tuple[bool, int]:
	if root == None:
		return True, 0
	isBalancedLeft, leftHeight = isBalancedHelper(root.left)
	isBalancedRight, rightHeight = isBalancedHelper(root.right)
	if isBalancedLeft == False or isBalancedRight == False:
		return False, -1
	if abs(leftHeight - rightHeight) <= 1:
		return True, max(leftHeight, rightHeight) + 1
	return False, -1


if __name__ == "__main__":
	root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
	assert isBalanced(root) == True
	
	left2 = TreeNode(3, TreeNode(4), TreeNode(4))
	left = TreeNode(2, left2, TreeNode(3))
	root = TreeNode(1, left, TreeNode(2))
	assert isBalanced(root) == False

	root = None
	assert isBalanced(root) == True