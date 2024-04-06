"""
Runtime: 271 ms beats 33%
Memory: 27.8 MB beats 9%
Time taken: 6 minutes however it took 3-4 more minutes to fix small issues

Iterate over all cells in the grid (x,y)
* Run DFS or BFS on each cell
* Store visited location
* On new visited cell, run DFS or BFS on neighbours

If we found new cell that is not visited, we increase island count
Only then we run the algo
"""
from typing import List
def numIslands(grid: List[List[str]]) -> int:
    island_count, visited = 0, set()

    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0' or (row, col) in visited:
            return
        # Current cell is not visited, add it and explore other cells
        visited.add((row, col))
        dfs(row, col+1)
        dfs(row, col-1)
        dfs(row+1, col)
        dfs(row-1, col)
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if grid[row_index][col_index] == '1' and (row_index, col_index) not in visited:
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