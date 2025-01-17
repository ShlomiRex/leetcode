"""

Runtime: beats 58%
Memory: beats 62%

"""

def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True
    if len(t) == 0:
        return len(s) == 0
    left, right = 0,0
    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            left += 1
            right += 1
        else:
            right += 1
    if left == len(s):
        return True
    return False

if __name__ == "__main__":
    assert isSubsequence("abc", "ahbgdc") == True
    assert isSubsequence("axc", "ahbgdc") == False
    assert isSubsequence("", "ahbgdc") == True
    assert isSubsequence("b", "c") == False
    assert isSubsequence("", "c") == True
    assert isSubsequence("c", "") == False
    assert isSubsequence("c", "c") == True
    assert isSubsequence("aaaaaa", "bbaaaa") == False