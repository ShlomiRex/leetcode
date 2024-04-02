"""
Runtime: 41 ms beats 67%
Memory: 16.69 MB beats 95%
Time taken: 36 minutes 11 seconds (very bad!!!!)

Observation: order of characters is the key point

egg add : E->A, G->D

foo bar : F->B, O->A, O->R cant have two mappings to different characters

i=0, F, B
if F in mappings: no
mappings = {F: B}

i=1, O, A
if O in mappings: no
mappings = {F: B, O: A}

i=2, O, R
if O in mappings: yes and if mappings[O] != R: yes
    return False

Wrong: 'badc' -> 'baba', expected: false
i=0, bb    {b:b}
i=1, aa    {b:b, a:a}
i=2, db    {b:b, a:a, d:b, b:d}
i=3, ca    


Wrong: 'paper' -> 'title', expected: true
i=0, pt         {p:t, t:p}
i=1, ai         {p:t, t:p, a:i, i:a}
i=2  pt         p in hashmap, mappings['p']='t', is 't' != 't'? No
                t in hashmap, mappings['t']='p', is 'p' != 'p'? No
"""
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    mappings = {}
    values = set()
    for i in range(len(s)):
        if s[i] not in mappings:
            # If the destination mapping already added, we can't map another (s[i]) to the same character
            if t[i] in values:
                return False
            mappings[s[i]] = t[i] # Add mappings
            values.add(t[i]) # Add destination mapping to set
        else:
            # mappings has key s[i]
            # The only OK situation is if the same key has the same mappings
            if mappings[s[i]] == t[i]:
                continue
            else:
                return False
    return True

if __name__ == "__main__":
    assert isIsomorphic("egg", "add") == True
    assert isIsomorphic("foo", "bar") == False
    assert isIsomorphic("paper", "title") == True
    