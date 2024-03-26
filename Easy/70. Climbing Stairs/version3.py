"""

Runtime: 41ms beats 13%
Memory: 16MB beats 31%

This is basically cheating, as we do the fibonnachi sequence. The real dynamic programming solution is shown in version 2.
"""
def climbStairs(n: int) -> int:
    if n <= 1:
        return n
    a, b = 1, 1
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
    return b

if __name__ == "__main__":
    assert climbStairs(1) == 1
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3
    assert climbStairs(4) == 5
    assert climbStairs(5) == 8
    