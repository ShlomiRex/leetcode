def makeGood(s: str) -> str:
    res = ""
    stack = []
    for c in s:
        if len(stack) > 0:
            head = stack[-1] # Peek head
            # If adj
            if head and c != head and c.lower() == head.lower():
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    return ''.join(stack)
    

if __name__ == "__main__":
    assert makeGood("leEeetcode") == "leetcode"
    assert makeGood("abBAcC") == ""
    assert makeGood("s") == "s"