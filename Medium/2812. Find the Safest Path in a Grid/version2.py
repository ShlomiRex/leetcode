"""
Time Limit Exceeded
Passed 1035/1036 test cases
"""
from typing import List
import heapq
def maximumSafenessFactor(grid: List[List[int]]) -> int:
    n = len(grid)
    # 1: Thief, 0: Empty cell

    thiefs = []
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 1:
                thiefs.append((row, col))
                grid[row][col] = 0
            else:
                grid[row][col] = float('inf')
    
    def getAdjIndInbounds(r, c):
        inds = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        ans = []
        for row, col in inds:
            if row >= 0 and row < n and col >= 0 and col < n:
                ans.append((row, col))
        return ans

    # Re-create the grid with distances
    # BFS - We need queue
    queue = thiefs[:]
    visited = set()
    while queue:
        r, c = queue.pop(0)
        if (r,c) in visited: continue
        visited.add((r, c))
        if grid[r][c] != 0:
            distance = 1 + min(grid[r][c] for r,c in getAdjIndInbounds(r, c))
            grid[r][c] = distance
        adjInds = getAdjIndInbounds(r, c)
        queue.extend(adjInds)
    
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
