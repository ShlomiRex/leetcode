"""
Runtime: 43 ms beats 36%
Memory: 16.5 MB beats 52%
Similar to Unique Paths, use DP
"""
from typing import List
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    # Initialize first row
    for col in range(cols):
        if obstacleGrid[0][col] == 0:
            dp[0][col] = 1
        else:
            break
    # Initialize first column
    for row in range(rows):
        if obstacleGrid[row][0] == 0:
            dp[row][0] = 1
        else:
            break
    # Iterate over all other cells
    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] = dp[row][col-1] + dp[row-1][col] if obstacleGrid[row][col] == 0 else 0
    return dp[rows-1][cols-1]

if __name__ == "__main__":
    #assert uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2
    #assert uniquePathsWithObstacles([[0,1],[0,0]]) == 1
    assert uniquePathsWithObstacles([[0],[1]]) == 0