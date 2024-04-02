"""
Runtime: 40 ms beats 72%
Memory: 32 MB beats 32%

We have 3 situations:

1. b->a then b->a again. This is OK. If we see the same source mapping to the same destination character, we can continue.
2. b->a then c->a. This is not OK because we can't have two mappings to the same character.
3. b->a then b->c. This is not OK because we can't have same source mapping to different destination characters.
"""
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    mappings, values = {}, set()
    for i in range(len(s)):
        # Check second situation
        if t[i] in values and s[i] not in mappings:
            return False
        # Check third situation
        if s[i] in mappings and mappings[s[i]] != t[i]:
            return False
        mappings[s[i]] = t[i]
        values.add(t[i])
    return True

if __name__ == "__main__":
    assert isIsomorphic("egg", "add") == True
    assert isIsomorphic("foo", "bar") == False
    assert isIsomorphic("paper", "title") == True
    