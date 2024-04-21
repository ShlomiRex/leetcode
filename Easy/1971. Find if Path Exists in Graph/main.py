"""
Runtime: 1579 ms beats 54%
Memory: 121MB beats 39%
Time taken: basic code: 15 minutes, fix errors: another 5-7 minutes.

Maybe use hashmap to store edges for O(1) lookup
Use recursion for each children
Use visited
"""
from typing import List
def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    Given: edges = [[0,1],[1,2],[2,0]]
    We create hashmap like so:
    {
        0: set(1, 2),
        1: set(0, 2),
        2: set(0, 1)
    }
    Notice both ends of each edge can act as key and a value.
    """
    hashmap = {}
    for i in range(n):
        hashmap[i] = set()
    # Edges are bidirectional, we can use one of the points on the edge as the key
    for edge in edges:
        hashmap[edge[0]].add(edge[1])
        hashmap[edge[1]].add(edge[0])

    visited = set()
    next_to_visit_queue = [source]
    while next_to_visit_queue: # While we have somewhere to visit
        curr = next_to_visit_queue.pop(0)
        if curr == destination: return True

        # If visited we don't want to visit again
        if curr in visited: continue
        visited.add(curr)

        # Add next children
        next_children = hashmap[curr]
        next_to_visit_queue.extend(next_children)
    return False
if __name__ == "__main__":
    assert validPath(3, [[0,1],[1,2],[2,0]], 0, 2) == True
    assert validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5) == False
    assert validPath(10, [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]], 7, 5) == True