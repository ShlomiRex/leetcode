"""
Runtime: 109 ms beats 39%
Memory: 17.04 MB beats 30%

Instead of constructing the string to be checked twice, we give l, r pointers, this was we don't need to slice the string at places where we want to delete character.
"""

def validPalindrome(s: str) -> bool:
    n = len(s)
    if n == 0 or n == 1: return True
    if n == 2 and s[0] == s[1]: return True
    
    def checkPalindromeWithoutDeletion(s, l, r):
        while l < r:
            if s[l] != s[r]: return False
            l, r = l+1, r-1
        return True
    
    l, r = 0, n-1
    while l < r:
        if s[l] != s[r]: return checkPalindromeWithoutDeletion(s, l+1, r) or checkPalindromeWithoutDeletion(s, l, r-1)
        l, r = l+1, r-1
    return True

if __name__ == "__main__":
    assert validPalindrome("aba") == True
    assert validPalindrome("abca") == True
    assert validPalindrome("abc") == False