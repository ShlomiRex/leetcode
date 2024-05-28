"""
Runtime: 61 ms beats 74%
Memory: 17.23 MB beats 70%

================================================================================

Optimized solutions compared to version 2

"""
def equalSubstring(s: str, t: str, maxCost: int) -> int:
    n, l, r, maxLength = len(s), 0, 0, 0
    while r < n:
        maxLength = max(maxLength, r-l)
        rCost = abs(ord(s[r]) - ord(t[r]))

        while rCost > maxCost:
            rCost -= abs(ord(s[l]) - ord(t[l]))
            l += 1
        
        maxCost -= rCost
        r += 1
    maxLength = max(maxLength, r-l)
    return maxLength


if __name__ == "__main__":
    assert equalSubstring("abcd", "bcdf", 3) == 3
    assert equalSubstring("abcd", "cdef", 3) == 1
    assert equalSubstring("abcd", "acde", 0) == 1
    assert equalSubstring("krrgw", "zjxss", 19) == 2
    assert equalSubstring("krpgjbjjznpzdfy", "nxargkbydxmsgby", 14) == 4

    assert equalSubstring("pxezla", "loewbi", 25) == 4
    