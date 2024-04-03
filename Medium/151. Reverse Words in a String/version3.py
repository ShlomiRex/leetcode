"""
Runtime: 43 ms beats 18%
Memory: 16.8 MB beats 8%
"""
def reverseWords(s: str) -> str:
    words = []
    i = len(s)
    while i >= 0:
        i -= 1
        word = []
        # Skip spaces
        while s[i] == ' ' and i >= 0:
            i -= 1
        # Collect word
        while s[i] != ' ' and i >= 0:
            word.append(s[i])
            i -= 1
        if not word:
            continue
        word = reversed(word)
        word = ''.join(word)
        words.append(word)

    return ' '.join(words)

if __name__ == "__main__":
    # s = "the sky is blue"
    # res = reverseWords(s)
    # assert res == "blue is sky the"

    s = "  hello world  "
    res = reverseWords(s)
    assert res == "world hello"

    s = "a good   example"
    res = reverseWords(s)
    assert res == "example good a"