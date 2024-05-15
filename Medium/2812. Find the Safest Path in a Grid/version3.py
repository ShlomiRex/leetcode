"""
Runtime: 5083 ms beats 31%
Memory: 21.29 MB beats 74%
"""
from collections import deque
from typing import List
import heapq
def maximumSafenessFactor(grid: List[List[int]]) -> int:
    n = len(grid)

    # Find thiefs, set to 'inf' distance if not thief, else, if thief, set distance to 0
    thiefs = []
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 1:
                thiefs.append((row, col))
                grid[row][col] = 0
            else:
                grid[row][col] = float('inf')
    
    def isInBounds(r, c):
        return min(r,c) >= 0 and max(r,c) < n

    queue = thiefs
    while queue:
        r, c = queue.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = r+dx, c+dy
            if isInBounds(new_x, new_y) and grid[new_x][new_y] == float('inf'):
                grid[new_x][new_y] = grid[r][c] + 1
                queue.append((new_x, new_y))
    
    # Max-heap. The distance is measured and compared.
    maxheap = []
    heapq.heappush(maxheap, (-grid[0][0], 0, 0))
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1

    while maxheap:
        dist, row, col = heapq.heappop(maxheap)
        dist = -dist # Normalize distance because of max heap (in python its min heap but we use minus to convert it to max heap)
        if row == n-1 and col == n-1:
            return dist
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_row, new_col = row + dx, col + dy
            if new_row >= 0 and new_row < n and new_col >= 0 and new_col < n and grid[new_row][new_col] != 0 and not visited[new_row][new_col]:
                visited[new_row][new_col] = 1
                new_dist = grid[new_row][new_col]
                heapq.heappush(maxheap, (- min(new_dist, dist), new_row, new_col))
    return 0
    
if __name__ == "__main__":
    assert maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]]) == 0
    assert maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]]) == 2
    assert maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]) == 2
