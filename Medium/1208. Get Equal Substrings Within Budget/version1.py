"""
Note: THIS SOLUTON DOESN'T WORK. Its just example of my thought process.

Traverse s
Calc cost of changing s[i] to t[i]
If we can change (lower than maxCost) then we change character, increase max length
"""
def equalSubstring(s: str, t: str, maxCost: int) -> int:
    n = len(s) # len(s) = len(t)
    maxLength = 0
    for i in range(n):
        if s[i] == t[i]:
            maxLength += 1
        else:
            cost = abs(ord(t[i]) - ord(s[i]))
            if cost <= maxCost:
                #s[i] = t[i] # We can say we switched
                maxCost -= cost
                maxLength += 1
            else:
                break
    return maxLength

if __name__ == "__main__":
    assert equalSubstring("abcd", "bcdf", 3) == 3
    assert equalSubstring("abcd", "cdef", 3) == 1
    assert equalSubstring("abcd", "acde", 0) == 1
    # This two tests don't work
    #assert equalSubstring("krrgw", "zjxss", 19) == 2
    #assert equalSubstring("krpgjbjjznpzdfy", "nxargkbydxmsgby", 14) == 4
    