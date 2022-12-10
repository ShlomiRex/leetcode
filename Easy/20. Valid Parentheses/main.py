# (}
def isValid(s: str) -> bool:
    if len(s) < 2:
        return False
    if len(s) % 2 != 0:
        return False
    
    allowed_pairs = {
		"{": "}",
		"[": "]",
		"(": ")"
	}
    
    stack = []
    for c in s:
        # If the character is an opening bracket, push it onto the stack.
        if c in allowed_pairs.keys():
            stack.append(c)
        # If the character is a closing bracket, pop the stack and check if the popped character is the corresponding one.
        else:
            if len(stack) == 0:
                return False
            head = stack.pop()
            if allowed_pairs[head] != c:
                return False
    return len(stack) == 0

if __name__ == "__main__":
	assert isValid("()") == True
	assert isValid("()[]{}") == True
	assert isValid("(]") == False
	assert isValid("([)]") == False
	assert isValid("{[]}") == True
	assert isValid("((") == False
	assert isValid("){") == False
