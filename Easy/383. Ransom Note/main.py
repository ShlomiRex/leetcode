"""

Runtime: beats 34%
Memory: beats 82.5%

"""

def canConstruct(ransomNote: str, magazine: str) -> bool:
    letters = {}
    for l in magazine:
        if l in letters: letters[l] += 1
        else: letters[l] = 1
    
    for c in ransomNote:
        if c not in letters: return False
        elif letters[c] == 0: return False
        else: letters[c] -= 1
    return True



if __name__ == "__main__":
    assert canConstruct("a", "b") == False
    assert canConstruct("aa", "ab") == False
    assert canConstruct("aa", "aab") == True