"""
Runtime: 1631 ms beats 31%
Memory: 17.5 MB beats 21%
Time taken: 2> hours, probably.

Looked at solutions of neetcode. Very complex.

Running complexity: O(26n) = O(n)
Memory complexity: O(26) = O(1)
"""
def longestIdealString(s: str, k: int) -> int:
    dp = [0] * 26
    for i in range(len(s)):
        curr_index, longest_ideal = ord(s[i]) - ord('a'), 1
        for prev in range(26):
            if abs(curr_index - prev) <= k:
                longest_ideal = max(longest_ideal, dp[prev] +1)
        dp[curr_index] = longest_ideal
    return max(dp)

if __name__ == "__main__":
    assert longestIdealString("acfgbd", 2) == 4
    assert longestIdealString("abcd", 3) == 4