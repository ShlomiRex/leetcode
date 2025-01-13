"""
Time complexity: O(len(words) * len(pref))
"""

from typing import List

def prefixCount(words: List[str], pref: str) -> int:
    n2 = len(pref)
    res = 0

    def starts_with(s: str) -> bool:
        if len(s) < n2: return False
        for i in range(n2):
            if pref[i] != s[i]:
                return False
        return True
    
    for word in words:
        if starts_with(word):
            res += 1
    
    return res

if __name__ == "__main__":
    words = ["pay","attention","practice","attend"]
    pref = "at"
    res = prefixCount(words, pref)
    assert res == 2

    words = ["leetcode","win","loops","success"]
    pref = "code"
    res = prefixCount(words, pref)
    assert res == 0