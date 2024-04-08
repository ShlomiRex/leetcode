"""
Runtime: 45 ms beats 10%
Memory: 17.2 MB beats 7%
Time taken: 1 hour

Not my solution. Without '@cache' I get Time Exceeded.
This is stupid.
"""
from functools import cache
def checkValidString(s: str) -> bool:
    n = len(s)
    @cache
    def backtrack(i, open_parenthesis_balance):
        if i == n: return open_parenthesis_balance == 0
        if open_parenthesis_balance < 0: return False
        res = False
        if s[i] == '(': res = backtrack(i+1, open_parenthesis_balance+1)
        elif s[i] == ')': res = backtrack(i+1, open_parenthesis_balance-1)
        else: res = backtrack(i+1, open_parenthesis_balance+1) or backtrack(i+1, open_parenthesis_balance-1) or backtrack(i+1, open_parenthesis_balance)
        return res
    return backtrack(0, 0)

if __name__ == "__main__":
    assert checkValidString("()") == True
    assert checkValidString("(*)") == True
    assert checkValidString("()") == True
    assert checkValidString("(*))") == True
    assert checkValidString("(") == False

