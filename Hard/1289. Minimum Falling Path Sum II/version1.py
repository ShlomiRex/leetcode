"""
Time limit exceeded, passed 6/16 test cases

I'm surprised this is the first solution that I did that works, although it doesn't pass all tests

Subproblem: given current row and chosen column, in the next row, what possible next elements we can choose? Answer: all elements except on the specific previous column.
"""
from typing import List
def minFallingPathSum(grid: List[List[int]]) -> int:
    n = len(grid)

    def calcPath(currRow, prevCol, currPathSum):
        if currRow >= n:
            return currPathSum
        minPathSum = float('inf')
        for col in range(n):
            # We chose grid[currRow+1][col]
            if col != prevCol:
                nextPathSum = calcPath(currRow+1, col, currPathSum+grid[currRow][col])
                minPathSum = min(minPathSum, nextPathSum)
        return minPathSum
    ans = float('inf')
    # First row we can choose any column
    for col in range(n):
        ans = min(ans, calcPath(1, col, grid[0][col]))
    return ans

if __name__ == "__main__":
    assert minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 13