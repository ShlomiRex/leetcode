"""
Runtime: 1393 ms beats 33.9%
Memory: 20.22 MB beats 20%

This is my own solution, probably took me 1 hour (including first solution)
"""
from typing import List
def minFallingPathSum(grid: List[List[int]]) -> int:
    n = len(grid)

    # init DP
    dp = [0] * n
    for i in range(n):
        dp[i] = [0] * n

    # Initialze first row
    for i in range(n):
        dp[0][i] = grid[0][i]
    
    for row in range(1, n):
        for col in range(n):
            minInPrevRow = float('inf')
            for col2 in range(n):
                if col2 != col and dp[row-1][col2] < minInPrevRow:
                    minInPrevRow = dp[row-1][col2]
            dp[row][col] = minInPrevRow + grid[row][col]
    return min(dp[n-1])

if __name__ == "__main__":
    assert minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 13
    assert minFallingPathSum([[7]]) == 7