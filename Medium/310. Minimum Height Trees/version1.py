"""
Time Limit Exceeded on test case 63/71

Step 1: Build tree
Step 2: Traverse each node of the tree and set each node as root
Step 3: Find minimum height by using BFS

This will be O(n^2)

Brute force approach
"""
from collections import defaultdict
from typing import List
def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    # Convert edges to hashset
    hashset_edges = defaultdict(list)
    for edge in edges:
        u, v = edge[0], edge[1]
        hashset_edges[u].append(v)
        hashset_edges[v].append(u)
    curr_min_height = float("inf")
    min_heights = set()
    for curr_root in range(n):
        queue = [(curr_root, 0)] # Node, height
        visited = set()
        tree_height = 0
        while queue:
            curr_node, curr_height = queue.pop(0)
            visited.add(curr_node)
            next_children = [(x, curr_height+1) for x in hashset_edges[curr_node] if x not in visited]
            if next_children:
                queue.extend(next_children)
            else:
                # We reached leaf: is the height of the tree greater, less than or equal to curr MHT?
                tree_height = max(tree_height, curr_height)

        # Check if tree height is MHT
        # We found new MHT
        if tree_height < curr_min_height:
            curr_min_height = tree_height
            min_heights = set()
            min_heights.add(curr_root)
        # Same height, append root to result
        elif tree_height == curr_min_height:
            min_heights.add(curr_root)
    return list(min_heights)

if __name__ == "__main__":
    assert findMinHeightTrees(4, [[1,0],[1,2],[1,3]]) == [1]
    assert findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]) == [3, 4]
    assert findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]) == [3]