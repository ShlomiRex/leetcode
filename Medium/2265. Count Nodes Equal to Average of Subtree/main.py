"""
Runtime: 28 ms beats 99%
Memory: 16 MB beats 18%
Time taken: 25 minutes
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def averageOfSubtree(root: TreeNode) -> int:
    ans = [0]
    def dfs(root) -> (int, int):
        if root is None:
            return 0, 0
        l_sum, l_num_nodes = dfs(root.left)
        r_sum, r_num_nodes = dfs(root.right)
        # We reached leafs first.
        _sum = l_sum + r_sum + root.val
        _num_nodes = l_num_nodes + r_num_nodes + 1
        _avg = _sum // _num_nodes
        if _avg == root.val:
            ans[0] += 1
        return _sum, _num_nodes
    dfs(root)
    return ans[0]

if __name__ == "__main__":
    l = TreeNode(8, TreeNode(0), TreeNode(1))
    r = TreeNode(5, None, TreeNode(6))
    tree = TreeNode(4, l, r)
    assert averageOfSubtree(tree) == 5

    tree = TreeNode(1)
    assert averageOfSubtree(tree) == 1