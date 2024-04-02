"""
Runtime: 51 ms beats 15%
Memory: 16.73 MB beats 64%

We have 3 situations:

1. b->a then b->a again. This is OK.
2. b->a then c->a. This is not OK because we can't have two mappings to the same character.
3. b->a then b->c. This is not OK because we can't have same source mapping to different destination characters.
"""
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    mappings = {}
    for i in range(len(s)):
        if s[i] not in mappings:
            if t[i] in mappings.values():
                return False
            mappings[s[i]] = t[i]
        else:
            if mappings[s[i]] != t[i]:
                return False
    return True

if __name__ == "__main__":
    assert isIsomorphic("egg", "add") == True
    assert isIsomorphic("foo", "bar") == False
    assert isIsomorphic("paper", "title") == True
    