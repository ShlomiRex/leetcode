"""
Runtime: 41 ms beats 13%
Memory: 16.5 MB beats 31%
Time taken: 4 minutes 26 seconds!
"""
def tribonacci(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1
    dp = [None] * (n+1)
    dp[0], dp[1], dp[2] = 0, 1, 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

if __name__ == "__main__":
    assert tribonacci(4) == 4
    assert tribonacci(25) == 1389537