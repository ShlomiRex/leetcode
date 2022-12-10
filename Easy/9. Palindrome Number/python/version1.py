def isPalindrome(x: int) -> bool:
	s = str(x)
	if x < 0:
		s = "-" + s

	i_low = 0
	i_high = len(s) - 1

	while i_low < i_high:
		low = s[i_low]
		high = s[i_high]
		if low != high:
			return False
		i_low += 1
		i_high -= 1
	return True

if __name__ == "__main__":
	x = 121
	assert isPalindrome(x) == True
	
	x = -121
	assert isPalindrome(x) == False

	x = 10
	assert isPalindrome(x) == False

	x = 1221
	assert isPalindrome(x) == True

	x = 1211
	assert isPalindrome(x) == False

	x = 5
	assert isPalindrome(x) == True