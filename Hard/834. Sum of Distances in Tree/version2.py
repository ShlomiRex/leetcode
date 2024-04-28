"""
Runtime: 832 ms beats 42%
Memory: 45 MB beats 49%
Time taken: 2 hours, couldn't complete alone, needed to see solutions. Brute force is easy.

We have to traverse entire tree anyway.
BFS? DFS?
Brute force: from each node i as root, calculate sum. 
The distance beteween node and root is the tree height, which can be done with BFS.
Runtime complexity: O(n * n)

But the optimized solution is O(n), here is link for explanation: https://www.youtube.com/watch?v=OCGPug-KirQ
Basically we use formula: given root=j and its parent=i:
    ans[j] = ans[i] + n - 2*count[j]
where count[i] is array of count number of nodes in subtree with root=i
"""
from typing import List
from collections import defaultdict
def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
    ans = [0] * n       # Final answer array
    count = [0] * n     # count[i] = number of nodes in subtree i where 0 is the root (including the root i of subtree)

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs1(curr, parent):
        count[curr] = 1
        for child in graph[curr]:
            if child != parent:
                dfs1(child, curr)
                count[curr] += count[child]
                ans[curr] += ans[child] + count[child]

    dfs1(0, None)

    def dfs2(curr, parent):
        for child in graph[curr]:
            if child != parent:
                ans[child] = ans[curr] + n - 2*count[child]
                dfs2(child, curr)
    
    dfs2(0, None)
    return ans

if __name__ == "__main__":
    assert sumOfDistancesInTree(n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]) == [8,12,6,10,10,10]
    assert sumOfDistancesInTree(n = 1, edges = []) == [0]
    assert sumOfDistancesInTree(n = 2, edges = [[1,0]]) == [1,1]