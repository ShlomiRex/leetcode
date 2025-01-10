from typing import List

"""
This solution is wrong. I thought the characters in subset must be in the same order as in the word we check.
But in the question, they ask for any order of the characters in the subset to be in the word.
"""

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    def is_word_subset(subset, word) -> bool:
        # Check if every letter in subset (wrr) is inside word (warrior)

        # If we can't fit
        if len(word) < len(subset):
            return False
        
        subset_i = 0
        for word_i in range(len(word)):
            if subset_i >= len(subset): 
                break
            if word[word_i] == subset[subset_i]:
                subset_i += 1
        res = subset_i == len(subset)
        if res:
            print(f"{subset} is a subset of {word}")
        else:
            print(f"{subset} is NOT a subset of {word}")
        return res
    
    def is_universal(a):
        # Check if word1 from words1 is universal string
        for b in words2:
            if not is_word_subset(b, a):
                return False
        return True
    
    res = []
    for a in words1:
        if is_universal(a):
            res.append(a)
    return res

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    pass
        
if __name__ == "__main__":
    #assert is_word_subset("wrr", "warrior") == True
    assert is_word_subset("wrr", "world") == False