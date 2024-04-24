"""
Runtime: 32 ms beats 74%
Memory: 16.4 MB beats 85%
Instead of using array of size (n+1) we can only keep track of last 3 elements.
"""
def tribonacci(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1
    a, b, c = 0, 1, 1
    for i in range(3, n):
        new_c = a+b+c
        a, b = b, c
        c = new_c
    return a+b+c

if __name__ == "__main__":
    assert tribonacci(4) == 4
    assert tribonacci(25) == 1389537