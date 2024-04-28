"""
Time limit exceeded, passed 64/74 test cases

BFS brute force solution.

We have to traverse entire tree anyway.
BFS? DFS?
Brute force: from each node i as root, calculate sum. 
The distance beteween node and root is the tree height, which can be done with BFS.
Runtime complexity: O(n * n)

I also thought about using the distance matrix, it looks good but its also O(n^2).
"""
from typing import List
from collections import defaultdict
def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
    ans = [0]*n
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(root) -> int:
        _sum = 0
        queue = [(root, 0, None)]
        while queue:
            curr, level, parent = queue.pop(0)
            #print(f"Node: {curr}, level: {level}")
            _sum += level
            for child in graph[curr]:
                if child != parent:
                    queue.append((child, level+1, curr))

        return _sum


    for i in range(n):
        #print(f"Root: {i}")
        ans[i] = bfs(i)
        #print(f"Sum: {ans[i]}\n")

    return ans

if __name__ == "__main__":
    assert sumOfDistancesInTree(n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]) == [8,12,6,10,10,10]
    assert sumOfDistancesInTree(n = 1, edges = []) == [0]
    assert sumOfDistancesInTree(n = 2, edges = [[1,0]]) == [1,1]