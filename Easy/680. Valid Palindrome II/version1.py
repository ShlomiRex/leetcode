"""
Runtime: 133 ms beats 12%
Memory: 16.8 MB beats 99%
Time taken: 13 minutes

Check palindrome. If found mismatch between characters s[i] != s[j] then we can delete one of them.
"""

def validPalindrome(s: str) -> bool:
    n = len(s)
    if n == 0 or n == 1:
        return True
    if n == 2 and s[0] == s[1]:
        return True
    
    def checkPalindromeWithoutDeletion(s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    l, r = 0, n-1

    while l < r:
        if s[l] != s[r]:
            # Either delete s[l] or delete s[r]
            return checkPalindromeWithoutDeletion(s[:l]+s[l+1:]) or checkPalindromeWithoutDeletion(s[:r]+s[r+1:])
        l += 1
        r -= 1
    return True

if __name__ == "__main__":
    assert validPalindrome("aba") == True
    assert validPalindrome("abca") == True
    assert validPalindrome("abc") == False