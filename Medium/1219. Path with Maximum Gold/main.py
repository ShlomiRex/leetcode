"""
Runtime: 5110 ms beats 9%
Memory: 16.5 MB beats 71%
Time taken: 17 minutes 2 seconds

grid[r][c] = amount of gold (0 is empty)
Its a decision tree, recursivly

[
    [1,0,7],
    [2,0,6],
    [3,4,5],
    [0,3,0],
    [9,0,20]
]
We can't be greedy, if we start with 9 we are finished. We can start at 1->2->3->4->5->6->7 which is more gold.
"""
from typing import List
def getMaximumGold(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    ans = 0

    def dfsMaxGold(row, col, visited, curr_gold):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return 0
        if (row, col) in visited or grid[row][col] == 0:
            return curr_gold

        visited.append((row, col))
        curr_gold += grid[row][col]
        #print(f"Visited: ({row},{col}), Grid gold: {grid[row][col]}, Curr gold: {curr_gold}")

        a = dfsMaxGold(row+1, col, visited[:], curr_gold)
        b = dfsMaxGold(row-1, col, visited[:], curr_gold)
        c = dfsMaxGold(row, col+1, visited[:], curr_gold)
        d = dfsMaxGold(row, col-1, visited[:], curr_gold)
        return max(a,b,c,d)
    
    # Start from any possible position
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != 0:
                ans = max(ans, dfsMaxGold(row, col, [], 0))
    return ans

if __name__ == "__main__":
    assert getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]) == 24
    assert getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]) == 28