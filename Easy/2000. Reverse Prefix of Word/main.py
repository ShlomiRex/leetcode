"""
Runtime: 37 ms beats 41%
Memory: 16.6 MB beats 9%
Time taken: 3 minutes 27 seconds

Check if ch exists
If not do nothing
If yes, reverse prefix
"""
def reversePrefix(self, word: str, ch: str) -> str:
    ch_ind = -1
    for i in range(len(word)):
        if word[i] == ch:
            ch_ind = i
            break
    # If found
    if ch_ind != -1:
        l, r, word = 0, ch_ind, list(word)
        while l < r:
            word[l], word[r] = word[r], word[l]
            l, r = l+1, r-1
        return "".join(word)
    # If not found, we do nothing
    return word