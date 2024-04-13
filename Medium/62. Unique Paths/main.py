"""
Runtime: 37 ms beats 48%
Memory: 16.64 MB beats 17%

I already knew that I had to use dp.
"""
def uniquePaths(m: int, n: int) -> int:
    dp = [[1]*n]*m # Create m x n zero matrix, then we overwrite first col and first row to be 1, then we overwrite from row=1 and col=1.
    for row in range(1, m):
        for col in range(1, n):
            dp[row][col] = dp[row-1][col] + dp[row][col-1]
    return dp[m-1][n-1]

if __name__ == "__main__":
    assert uniquePaths(3, 7) == 28
    assert uniquePaths(3, 2) == 3