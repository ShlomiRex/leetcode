"""

Runtime: 40ms beats 41%
Memory: 16 MB beats 42%
Time taken: more than 45 minutes. I didn't have the knowledge of backtracking algorithm.

Solution:
My first intuition was to use recursion, like: () -> (_) or ()_ which gets: (()) or ()() but we get multiple duplicate strings.

I looked for neetcode general idea. Its basically backtracking algorithm.

We choose to either add '(' or ')' at the current decision tree.
We have 'open' and 'close' counters to indicate how many open/close parenthesis we can use.

We add '(' only if open > 0
We add ')' only if close < open (and not equal or greater than)

"""
from typing import List

def generateParenthesis(n: int) -> List[str]:
    res = []

    # Its like DFS we need to find the leafs
    def dfs(curr: str, _open: int, _close: int):
        # Check leaf
        if _open == _close == 0:
            res.append(curr)
            return
        # Add open parenthesis
        if _open > 0:
            dfs(curr+"(", _open-1, _close)
        # Add close parenthesis
        # Because its recursion, we don't ask 'elif', we have 2 choices per each node.
        if _open < _close:
            dfs(curr+")", _open, _close-1)

    dfs("", n, n)

    return res

if __name__ == "__main__":
    assert generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]
    assert generateParenthesis(1) == ["()"]
    assert generateParenthesis(2) == ["(())","()()"]
    assert generateParenthesis(4) == ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
