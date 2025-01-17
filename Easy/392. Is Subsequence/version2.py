"""
Time taken: 5:22

"""

def isSubsequence(s: str, t: str) -> bool:
    if len(t) < len(s):
        return False
    s_i = 0
    for i in range(len(t)):
        if s_i >= len(s): break
        if t[i] == s[s_i]:
            s_i += 1
    return s_i == len(s)

if __name__ == "__main__":
    assert isSubsequence("abc", "ahbgdc") == True
    assert isSubsequence("axc", "ahbgdc") == False
    assert isSubsequence("", "ahbgdc") == True
    assert isSubsequence("b", "c") == False
    assert isSubsequence("", "c") == True
    assert isSubsequence("c", "") == False
    assert isSubsequence("c", "c") == True
    assert isSubsequence("aaaaaa", "bbaaaa") == False