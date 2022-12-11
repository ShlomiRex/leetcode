def minAddToMakeValid(s: str) -> int:
	if len(s) == 0:
		return 0
	stack = []
	for c in s:
		if c == "(":
			stack.append(c)
		else:
			if len(stack) > 0 and stack[-1] == "(":
				stack.pop()
			else:
				stack.append(c)
	return len(stack)

if __name__ == "__main__":
	s = "())"
	assert minAddToMakeValid(s) == 1
	
	s = "((("
	assert minAddToMakeValid(s) == 3

	s = "()"
	assert minAddToMakeValid(s) == 0

	s = "()))"
	assert minAddToMakeValid(s) == 2

	s = "((()))"
	assert minAddToMakeValid(s) == 0

	s = "((((((()))"
	assert minAddToMakeValid(s) == 4