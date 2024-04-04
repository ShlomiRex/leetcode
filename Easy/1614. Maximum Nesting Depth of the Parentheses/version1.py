"""
Runtime: 42 ms beats 11%
Memory: 16.5 MB beats 38%
Time taken: 8 minutes


Two pointer: l, r
Search for open parenthesis for l
Search for close parenthesis for r
We reached the first parenthesis, depth 1

Maybe stack? This might be better

Then we can optimize without a stack, just curr and max nesting depth
"""
def maxDepth(s: str) -> int:
    max_nesting_depth = 0
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
            max_nesting_depth = max(max_nesting_depth, len(stack))
        elif s[i] == ')':
            stack.pop()
    return max_nesting_depth

if __name__ == "__main__":
    assert maxDepth("(1+(2*3)+((8)/4))+1") == 3
    assert maxDepth("(1)+((2))+(((3)))") == 3
