"""
Runtime: 30ms beats 90%
Memory: 16MB beats 57%
"""

def lengthOfLastWord(s: str) -> int:
    l, last_word_length, word_started = len(s), 0, False
    for i in range(l - 1, -1, -1):
        if s[i] == ' ' and word_started:
            break
        if s[i] != ' ':
            last_word_length, word_started = last_word_length+1, True
    return last_word_length

if __name__ == "__main__":
    assert lengthOfLastWord("Hello World") == 5
    assert lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert lengthOfLastWord("luffy is still joyboy") == 6