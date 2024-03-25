"""
Version 1

Coding time: 16 minutes

Runtime: 84 ms beats 45%
Memory: 17.7 MB beats 98%

"""

def minRemoveToMakeValid(s: str) -> str:
    # 0 Length
    if s is None or "":
        return ""
    
    # 1 Length
    if len(s) == 1:
        if s == ")" or s == "(":
            return ""
        return s
    
    # >2 Length
    # TODO: Change change stack to some integer representing how much '(' we agregated
    stack = []
    i = 0

    while i < len(s):
        c = s[i]
        if c == ')' and len(stack) == 0:
            s = s[:i] + s[i+1:] # Delete character
            continue
        if c == ')' and len(stack) > 0:
            stack.pop()
        if c == '(':
            stack.append('(')
        i += 1

    # While stack not empty, iterate in reverse order
    i = len(s) - 1
    while len(stack) != 0:
        c = s[i]
        if c == '(':
            s = s[:i] + s[i+1:] # Delete character
            stack.pop()
        i = i - 1

    return s


if __name__ == "__main__":
    ans = minRemoveToMakeValid("lee(t(c)o)de)")
    assert ans == "lee(t(c)o)de" or "lee(t(co)de)" or "lee(t(c)ode)"

    ans = minRemoveToMakeValid("a)b(c)d")
    assert ans == "ab(c)d"

    ans = minRemoveToMakeValid("))((")
    assert ans == ""

    assert minRemoveToMakeValid("") == ""

    ans = minRemoveToMakeValid("()")
    assert ans == "()"

    ans = minRemoveToMakeValid("()()")
    assert ans == "()()"

    ans = minRemoveToMakeValid("())")
    assert ans == "()"

    ans = minRemoveToMakeValid(None)
    assert ans == ""

    ans = minRemoveToMakeValid("(")
    assert ans == ""

    ans = minRemoveToMakeValid(")")
    assert ans == ""

    ans = minRemoveToMakeValid(")()")
    assert ans == "()"

    ans = minRemoveToMakeValid("((()))")
    assert ans == "((()))"

    ans = minRemoveToMakeValid("(((()))")
    assert ans == "((()))"

    ans = minRemoveToMakeValid("l")
    assert ans == "l"
