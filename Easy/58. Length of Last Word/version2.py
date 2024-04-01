"""
Runtime: 34 ms beats 61%
Memory: 16 MB beats 27%
Time taken: 3 minutes 44 seconds
"""

def lengthOfLastWord(s: str) -> int:
    last_word_len = 0
    letter_hit = False
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            letter_hit = True
            last_word_len += 1
        if s[i] == ' ' and letter_hit:
            return last_word_len
    return last_word_len

if __name__ == "__main__":
    assert lengthOfLastWord("Hello World") == 5
    assert lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert lengthOfLastWord("luffy is still joyboy") == 6