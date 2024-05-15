"""
Time Limit Exceeded
Time taken: 51 minutes 32 seconds
Passed 528/1036 test cases

==============================================================================

Maybe we can first calculate for each cell distances to closest thief?
Given:
[
    [0,0,0,1],
    [0,0,0,0],
    [0,0,0,0],
    [1,0,0,0]
]
We can get:
[
    [3,2,1,0],
    [2,3,2,1],
    [1,2,3,2],
    [0,1,2,3]
]
Path: [3, 2, 3, 2, 3, 2, 3]
Minimum safest distance: 2.

Given:
[
    [0,0,1],
    [0,0,0],
    [0,0,0]
]
We get:
[
    [2,1,0],
    [3,2,1],
    [4,3,2]
]
Path: [2, 3, 4, 3, 2]
Minimum safest distance: 2

Given:
[
    [1,0,0],
    [0,0,0],
    [0,0,1]
]
We get:
[
    [0,1,2],
    [1,2,1],
    [2,1,0]
]
Path: [0, 1, 2, 1, 0]
Minimum safest distance: 0

"""
from typing import List
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
    
    def getAdjInd(r, c):
        inds = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        ans = []
        for row, col in inds:
            if row >= 0 and row < n and col >= 0 and col < n:
                ans.append((row, col))
        return ans

    def getMinAdjDistance(r, c):
        adjInds = getAdjInd(r, c)
        minAdjDistance = float('inf')
        for row, col in adjInds:
            minAdjDistance = min(minAdjDistance, grid[row][col])
        return minAdjDistance

    # Re-create the grid with distances
    # BFS - We need queue
    queue = thiefs[:]
    visited = set()
    while queue:
        r, c = queue.pop(0)
        if (r,c) in visited:
            continue
        visited.add((r, c))
        if grid[r][c] != 0:
            distance = 1 + getMinAdjDistance(r, c)
            grid[r][c] = distance
        adjInds = getAdjInd(r, c)
        queue.extend(adjInds)
    
    def getMinSafestPathDFS(curr_row, curr_col, curr_min_distance):
        if curr_row < 0 or curr_row >= n or curr_col < 0 or curr_col >= n:
            return 0

        curr_min_distance = min(curr_min_distance, grid[curr_row][curr_col])

        if curr_row == n-1 and curr_col == n-1:
            return curr_min_distance
        
        a = getMinSafestPathDFS(curr_row+1, curr_col, curr_min_distance)
        b = getMinSafestPathDFS(curr_row, curr_col+1, curr_min_distance)
        curr_min_distance = max(a, b)

        return curr_min_distance
    
    return getMinSafestPathDFS(0,0,float('inf'))

if __name__ == "__main__":
    assert maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]]) == 0
    assert maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]]) == 2
    assert maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]) == 2
