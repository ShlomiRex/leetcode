def reverseWords(s: str) -> str:
    rev_words = s.lstrip().rstrip().split()
    rev_words.reverse()
    return ' '.join(rev_words)

if __name__ == "__main__":
    s = "the sky is blue"
    res = reverseWords(s)
    assert res == "blue is sky the"

    s = "  hello world  "
    res = reverseWords(s)
    assert res == "world hello"

    s = "a good   example"
    res = reverseWords(s)
    print(res)
    assert res == "example good a"