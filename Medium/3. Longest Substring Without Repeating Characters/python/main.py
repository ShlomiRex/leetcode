
# abcabcbb
#i   
# j       
def lengthOfLongestSubstring(s: str) -> int:
    l, charSet, longest_ss = 0, set(), 0 # Contains all unique characters, also checking for a character in the set is O(1)
    # We don't know how to initialize the right pointer so we have for loop and while loop
    for r in range(len(s)):
        # While the s[r] in our charset, we need to shrink the left window and remove the left character from the charSet and shrink left window
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r]) # After removed all duplicates, the s[r] doesn't appear in charset so we can safely add it
        longest_ss = max(longest_ss, r - l + 1)
    return longest_ss
            
if __name__ == "__main__":
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("") == 0
