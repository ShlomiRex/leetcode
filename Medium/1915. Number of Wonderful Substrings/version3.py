"""

Read previous versions of the code
Video explaining: https://www.youtube.com/watch?v=6jDMVwOXb2E
"""
from collections import defaultdict, Counter
def wonderfulSubstrings(word: str) -> int:
    ans = 0
    count = defaultdict(int)
    bitmasks = 0

    count[0] = 1 # All bitmasks are off, which means count of '0' is 1 at the start.
    for char in word:
        ind = ord(char) - ord('a')
        bitmasks ^= (1 << ind)
        ans += count[bitmasks]
        # TODO: Understand why we do this V
        for i in range(10):
            bitmasks ^= (1 << i)
            ans += count[bitmasks]
            bitmasks ^= (1 << i)
        count[bitmasks] += 1
    return ans

if __name__ == "__main__":
    assert wonderfulSubstrings("aba") == 4
    assert wonderfulSubstrings("aabb") == 9
    assert wonderfulSubstrings("he") == 2