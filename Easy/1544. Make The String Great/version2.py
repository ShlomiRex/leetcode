"""
Runtime: 34 ms beats 78%
Memory: 16.5 MB beats 46%
"""
def makeGood(s: str) -> str:
    stack = []
    for c in s:
        if stack: # If stack not empty
            head = stack[-1] # Peek head
            if head and c != head and c.lower() == head.lower(): # If adj
                stack.pop()
                continue
        stack.append(c)
    return ''.join(stack)
    

if __name__ == "__main__":
    assert makeGood("leEeetcode") == "leetcode"
    assert makeGood("abBAcC") == ""
    assert makeGood("s") == "s"