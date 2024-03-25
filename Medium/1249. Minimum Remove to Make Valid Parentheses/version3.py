"""
Version 3

Runtime: 65 ms beats 83%
Memory: 18 MB beats 71%

Idea: keep track of the index of open paranthesis, don't remove characters while iterating
After first iteration, remove all the characters from the string at the stored indexs

We can store the indexes in a stack
If python if your iterating over string, its more performant to convert it to list.

"""

def minRemoveToMakeValid(s: str) -> str:
    s = list(s)
    open_paranthesis_indexes_stack = []
    for i, c in enumerate(s):
        if c == '(':
            open_paranthesis_indexes_stack.append(i) # Store index of open paranthesis
        elif c == ')':
            if open_paranthesis_indexes_stack:
                open_paranthesis_indexes_stack.pop() # Remove last added index. This indicates that we completed a valid paranthesis string '(...)' so we don't need to remove the occurance of '('
            else:
                s[i] = '' # Remove excess close paranthesis. Because we iterate over list, here we won't affect our index (change character from list, not remove character from string)
    
    # Remove excess open paranthesis
    while open_paranthesis_indexes_stack:
        s[open_paranthesis_indexes_stack.pop()] = ''
    
    # Return the list (note: we have some empty characters: '' but we don't need to show it)
    return ''.join(s)
    


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
