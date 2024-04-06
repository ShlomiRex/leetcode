"""
Runtime: 243 ms beats 62%
Memory: 18.9 MB beats 61%

In this version, we don't need to keep set of visited cells.
We can modify the grid itself to mark visited cells.
"""
from typing import List
def numIslands(grid: List[List[str]]) -> int:
    island_count = 0

    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
            return
        # Current cell is not visited, mark it, add it and explore other cells
        grid[row][col] = ''
        dfs(row, col+1)
        dfs(row, col-1)
        dfs(row+1, col)
        dfs(row-1, col)
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if grid[row_index][col_index] == '1':
                island_count += 1
                dfs(row_index, col_index)
    return island_count

if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert numIslands(grid) == 1

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert numIslands(grid) == 3