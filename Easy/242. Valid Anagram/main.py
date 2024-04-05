"""
Runtime: 43 ms beats 85%
Memory: 17 MB beats 64%
Time taken: 7 minutes

return if t is an anagram of s

Iterate over characters in s, add to hashset, and count frequency
Do the same thing for t
And compare both hashmaps. Since order of characters doesn't matter. The only thing that matters is if there are enough letters in t as s.

We can optimize: instead of 2 loops, do it in one. The length of both strings must be the same.

We can further optimize: instead of one hashmap, for 't' we increase frequency, and for 's' we decrease frequency. The frequency must match 0 for all keys.
"""
from collections import defaultdict
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    hashmap = defaultdict(int) # Because we count frequencies, default value is 0.
    for i in range(len(s)):
        hashmap[s[i]] += 1
        hashmap[t[i]] -= 1
    for key in hashmap:
        if hashmap[key] != 0:
            return False
    return True

if __name__ == "__main__":
    assert isAnagram("anagram", "nagaram") == True
    assert isAnagram("rat", "car") == False