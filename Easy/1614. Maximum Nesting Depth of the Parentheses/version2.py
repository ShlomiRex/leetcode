"""
Runtime: 26 ms beats 96%
Memory: 16.5 MB beats 90%
"""
def maxDepth(s: str) -> int:
    max_nesting_depth, curr_nesting_depth = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            curr_nesting_depth += 1
            max_nesting_depth = max(max_nesting_depth, curr_nesting_depth)
        elif s[i] == ')':
            curr_nesting_depth -= 1
    return max_nesting_depth

if __name__ == "__main__":
    assert maxDepth("(1+(2*3)+((8)/4))+1") == 3
    assert maxDepth("(1)+((2))+(((3)))") == 3
