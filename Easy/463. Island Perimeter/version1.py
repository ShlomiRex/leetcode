"""
Runtime: 387 ms beats 59%
Memory: 18.16 MB beats 30%
Time taken: 16 minutes

Because there is exactly one island we can go and find first '1' and start DFS.
"""
from typing import List
def islandPerimeter(grid: List[List[int]]) -> int:
    ans = [0]
    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
            ans[0] += 1
            return
        if grid[row][col] == -1: 
            return
        grid[row][col] = -1 # Mark visited
        dfs(row, col+1)
        dfs(row, col-1)
        dfs(row-1, col)
        dfs(row+1, col)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                dfs(row, col)
                return ans[0]
    # We 100% Know there is exactly least one island
if __name__ == "__main__":
    assert islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
    assert islandPerimeter([[1]]) == 4
    assert islandPerimeter([[1,0]]) == 4