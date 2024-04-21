"""
Runtime: 431 ms beats 43%
Memory: 18.07 MB beats 32%

Although this version is more elegant, its slower, since we traverse entire matrix, instead of flood fill the island.
"""
from typing import List
def islandPerimeter(grid: List[List[int]]) -> int:
    ans = 0
    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
            return 1
        if grid[row][col] == -1: 
            return 0
        grid[row][col] = -1 # Mark visited
        return dfs(row, col+1) + dfs(row, col-1) + dfs(row-1, col) + dfs(row+1, col)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                ans += dfs(row, col)
    return ans
if __name__ == "__main__":
    assert islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
    assert islandPerimeter([[1]]) == 4
    assert islandPerimeter([[1,0]]) == 4