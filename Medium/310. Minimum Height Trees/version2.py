"""
Runtime: 474 ms beats 15%
Memory: 27 MB beats 72%

I took a look at solutions. This is a new trick I learned: to use BFS to remove leafs like an onion until we reach the center of the graph.
"""
from collections import defaultdict
from typing import List
def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1: return [0]
    # Convert edges to hashset
    hashset_edges = {}
    degrees = [0] * n
    for edge in edges:
        u, v = edge[0], edge[1]
        if u in hashset_edges:
            hashset_edges[u].append(v)
        else:
            hashset_edges[u].append(v)
        hashset_edges[v].append(u)
        degrees[u] += 1
        degrees[v] += 1

    # Iterate over leafs first
    queue = []
    for i in range(n):
        if degrees[i] == 1:
            queue.append(i)
    total_nodes = n
    # We don't ask len(queue) > 2 because we can have triangle: 3->0, 3->4 so we have 2 leafs but the answer is 3.
    while total_nodes > 2:
        # Delete batch of leafs
        num_leafs = len(queue)
        total_nodes -= num_leafs
        for _ in range(num_leafs):
            leaf = queue.pop(0)
            for neighbor in hashset_edges[leaf]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 1:
                    queue.append(neighbor)  
    return list(queue)


if __name__ == "__main__":
    assert findMinHeightTrees(4, [[1,0],[1,2],[1,3]]) == [1]
    assert findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]) == [3, 4]
    assert findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]) == [3]