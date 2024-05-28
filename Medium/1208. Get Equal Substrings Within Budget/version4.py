"""
Runtime: 61 ms beats 74%
Memory: 17.23 MB beats 70%

================================================================================

I looked at solutions.
"""
def equalSubstring(s: str, t: str, maxCost: int) -> int:
    N = len(s)
    max_len = 0
    # Starting index of the current substring
    start = 0
    # Cost of converting the current substring in s to t
    curr_cost = 0
    
    for i in range(N):
        # Add the current index to the substring
        curr_cost += abs(ord(s[i]) - ord(t[i]))
        
        # Remove the indices from the left end till the cost becomes less than the allowed
        while curr_cost > maxCost:
            curr_cost -= abs(ord(s[start]) - ord(t[start]))
            start += 1
        
        max_len = max(max_len, i - start + 1)
    
    return max_len


if __name__ == "__main__":
    assert equalSubstring("abcd", "bcdf", 3) == 3
    assert equalSubstring("abcd", "cdef", 3) == 1
    assert equalSubstring("abcd", "acde", 0) == 1
    assert equalSubstring("krrgw", "zjxss", 19) == 2
    assert equalSubstring("krpgjbjjznpzdfy", "nxargkbydxmsgby", 14) == 4
    print(equalSubstring("pxezla", "loewbi", 25))