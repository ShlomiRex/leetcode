"""
Runtime: 40 ms beats 33%
Memory: 16.7 MB beats 80%
"""
def reverseWords(s: str) -> str:
    return ' '.join(reversed(s.split()))

if __name__ == "__main__":
    s = "the sky is blue"
    res = reverseWords(s)
    assert res == "blue is sky the"

    s = "  hello world  "
    res = reverseWords(s)
    assert res == "world hello"

    s = "a good   example"
    res = reverseWords(s)
    assert res == "example good a"