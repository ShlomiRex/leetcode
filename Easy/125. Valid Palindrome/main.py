def isPalindrome(s: str) -> bool:
	if s == None or len(s) == 1:
		return True
	i_l, i_h = 0, len(s)-1
	s = s.lower()
	while i_l <= i_h:
		l, h = s[i_l], s[i_h]
		if (l < 'a' or l > 'z') and l.isdigit() == False:
			i_l += 1
			continue
		if (h < 'a' or h > 'z') and h.isdigit() == False:
			i_h -= 1
			continue
		if l != h:
			return False
		i_l, i_h = i_l+1, i_h-1
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

