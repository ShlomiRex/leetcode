"""
Time taken: 1 hour
Runtime complexity: has_circle: O(n * edges), is_one_component: O(n)

Valid graph if we have one component and no cycle

One component: we run DFS on the first node. Then we loop on all other nodes, if we visited them all, then we have one component.

No cycle: we run DFS, we check if the next node is not our parent (or grandparent or grandgrandparent and so on). IF all nodes match this, then we have no cycle.
"""

from typing import Optional, List

class Node:
    def __init__(self, value: int):
        self.value = value
        self.edges = []
        self.visited = False
    
    def add_edge(self, node: 'Node'):
        self.edges.append(node)

def validTree(n: int, edges: List[List[int]]) -> bool:
    if n < 2:
        return True

    nodes = []
    for i in range(n):
        nodes.append(Node(i))

    # Construct graph with edges
    for edge in edges:
        start = edge[0]
        end = edge[1]
        nodes[start].add_edge(nodes[end])
        nodes[end].add_edge(nodes[start])
    
    # Check has one component
    def has_circle(root: Optional[Node], direct_parent: Optional[Node]):
        if not root:
            return False
        
        if root.visited:
            return True

        # print(f"Visited: {root.value}")
        root.visited = True

        res = False
        for edge_end in root.edges:
            # If we have parent, and the edge is connected to parent, don't go back to parent, only to children, check has_circle for children only
            if not (direct_parent and edge_end.value == direct_parent.value):
                if has_circle(edge_end, root):
                    return True
        return False
    
    def is_one_component():
        for node in nodes:
            if node.visited == False:
                # print(f"Did not visit: {node.value}")
                return False
        return True
    
    circle = has_circle(nodes[0], None)
    is_one_comp = is_one_component()
    # print(f"circle = {circle}, is_one_component: {is_one_comp}")

    return (circle == False) and (is_one_comp)

if __name__ == "__main__":
    assert validTree(5, [[0,1],[0,2],[0,3],[1,4]]) == True
    assert validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]) == False
    assert validTree(2, [[1,0]]) == True
    assert validTree(2, []) == False
