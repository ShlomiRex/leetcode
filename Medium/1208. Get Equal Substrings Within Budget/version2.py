"""
Runtime: 91 ms beats 5%
Memory: 18.04 MB beats 17%
Time taken: 27 minutes 47 seconds

================================================================================

I looked at solutions. Apperantly I did not understand that they are looking for largest continous substring, and not largest substring from index 0.

Complexity: O(n)
"""
def equalSubstring(s: str, t: str, maxCost: int) -> int:
    n = len(s) # len(s) = len(t)
    diff = [abs(ord(t[i]) - ord(s[i])) for i in range(n)]
    l, r = 0, 0
    maxLength = 0
    while r < n:
        maxLength = max(maxLength, r-l)
        rCost = abs(ord(s[r]) - ord(t[r]))
        if rCost <= maxCost:
            maxCost -= rCost
            r += 1
        else:
            maxCost += abs(ord(s[l]) - ord(t[l]))
            l += 1
    maxLength = max(maxLength, r-l)
    return maxLength


if __name__ == "__main__":
    assert equalSubstring("abcd", "bcdf", 3) == 3
    assert equalSubstring("abcd", "cdef", 3) == 1
    assert equalSubstring("abcd", "acde", 0) == 1
    assert equalSubstring("krrgw", "zjxss", 19) == 2
    assert equalSubstring("krpgjbjjznpzdfy", "nxargkbydxmsgby", 14) == 4
    