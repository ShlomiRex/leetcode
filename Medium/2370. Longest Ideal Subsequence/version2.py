"""
Sort of brute force solution
Doesn't pass tests, time limit exceeded
76/85 tests passed

The time complexity is O(2^n) however because we use prev character, for each character s[i] the prev can be up to 26 characters away, so O(n * 26)
"""
def longestIdealString(s: str, k: int) -> int:
    n = len(s)
    if n == 1: return 1
    if k > 25: return n

    cache = {}
    # Helper function returns the length of the longest ideal string at index i
    # The 'prev' character represents the last character in the path, we can skip characters in the backtracking tree.
    def helper(i: int, prev: chr):
        if i == n: return 0
        if (i, prev) in cache: return cache[(i, prev)]
        res = helper(i+1, prev) # Don't include current element
        if prev == '' or abs(ord(s[i]) - ord(prev)) <= k:
            res = max(res, helper(i+1, s[i]) + 1)         # Include current element
        cache[(i, prev)] = res
        return res
    return helper(0, '')

if __name__ == "__main__":
    assert longestIdealString("acfgbd", 2) == 4
    assert longestIdealString("abcd", 3) == 4