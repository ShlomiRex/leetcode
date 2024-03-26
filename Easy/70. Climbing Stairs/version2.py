"""

Runtime: 36ms beats 47%
Memory: 16MB beats 31%

I use my previous knowledge (version1) to know that we can't store the combinations of climbing stairs.
Instead we must store a number. So we convert the dp list into a number.

Note: I took a look for neetcode explanation. Its indeed true 'dp' question, but instead we do bottom-up approach (start with i=n, then solve for i=n-1, ...)
Note: its best explained in my personal notebook, with sketches.
"""
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    dp = [0]*(n+1) # Including 0...n
    dp[-1], dp[-2] = 1, 1 # Its always going to be like this
    for i in range(n-2, -1, -1): # Stop index is inclusive (we must access dp[0])
        dp[i] = dp[i+1] + dp[i+2]
    return dp[0]

if __name__ == "__main__":
    assert climbStairs(1) == 1
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3
    assert climbStairs(4) == 5
    assert climbStairs(5) == 8
    