"""
Version 2

Runtime: 67 ms beats 79%
Memory: 17.6 MB beats 99%

"""

def minRemoveToMakeValid(s: str) -> str:
    if s is None or "":
        return ""
    
    if len(s) == 1:
        if s == ")" or s == "(":
            return ""
        return s
    
    i, open_parenthesis_counter = 0, 0

    while i < len(s):
        c = s[i]
        if c == ')' and open_parenthesis_counter == 0:
            s = s[:i] + s[i+1:] # Delete character
            continue
        if c == ')' and open_parenthesis_counter > 0:
            open_parenthesis_counter -= 1
        if c == '(':
            open_parenthesis_counter += 1
        i += 1

    # While stack not empty, iterate in reverse order
    i = len(s) - 1
    while open_parenthesis_counter != 0:
        c = s[i]
        if c == '(':
            s = s[:i] + s[i+1:] # Delete character
            open_parenthesis_counter -= 1
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
