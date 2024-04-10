"""
Runtime: 62 ms beats 7.4%
Memory: 16.95 MB beats 91%
Time taken: 13 minutes
"""
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    def isAlphaNumeric(c):
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))
    while left < right:
        while left < right and not isAlphaNumeric(s[left]):
            left += 1
        while left < right and not isAlphaNumeric(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
	s = "A man, a plan, a canal: Panama"
	assert isPalindrome(s) == True

	s = "race a car"
	assert isPalindrome(s) == False

	s = " "
	assert isPalindrome(s) == True

	s = ""
	assert isPalindrome(s) == True

	s = "0P"
	assert isPalindrome(s) == False

	s = "ab2a"
	assert isPalindrome(s) == False

