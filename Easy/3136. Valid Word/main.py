"""
Runtime: 41 ms beats 100%
Memory: 16.6 MB beats 100%
"""
def isValid(word: str) -> bool:
    vowel = ['a', 'e', 'i', 'o', 'u']
    if len(word) < 3:
        return False
    at_least_one_vowel = False
    at_least_one_consonant = False
    for c in word:
        if c.isalnum() == False:
            return False
        if c.lower() in vowel:
            at_least_one_vowel = True
        elif ord(c.lower()) >= ord('a') and ord(c.lower()) <= ord('z'):
            at_least_one_consonant = True
    if at_least_one_vowel == False or at_least_one_consonant == False:
        return False
    return True

if __name__ == "__main__":
    assert isValid("234Adas") == True
    assert isValid("b3") == False
    assert isValid("a3$e") == False
    assert isValid("UuE6") == False

    