"""

Runtime: 40ms beats 56%
Memory: 17.19 MB beats 92%
Time taken: 19 minutes 26 seconds, though I had to read explanation of BFS, I had some interruptions.

First intuition:
Use queue
Add current root/node to the queue
Then add left to the queue
Then add right to the queue

While queue not empty:
    next_node = queue.pop
    res.append(next_node)

    

After I read some BFS explanation:

The problem is to know what to append to answer. I need to append all the nodes of a single tree height.
How? The queue helps us. The size of the queue is the size of the current level. So I can iterate over the size of the queue and append all the nodes of that level to temporary array.
This temporary array is the current level of the tree. Then I append this temporary array to the answer.
"""
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    ans = []
    queue = [root]
    
    while queue:
        current_level = [] # Current level holds all the nodes of a single tree height
        level_size = len(queue) # Size of queue is changing in the for loop, so we store snapshot of it here. Indicates number of nodes in the current level
        for _ in range(level_size):
            node = queue.pop(0) # First in first out
            current_level.append(node.val)
            if node.left: # We ask this so we don't insert None to queue (and get error to get its value)
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(current_level)       
    return ans

if __name__ == "__main__":
    l = TreeNode(9)
    r = TreeNode(20, TreeNode(15), TreeNode(7))
    root = TreeNode(3, l, r)
    assert levelOrder(root) == [[3],[9,20],[15,7]]

    assert levelOrder(None) == []

