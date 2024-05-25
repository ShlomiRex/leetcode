"""
Runtime: 37 ms beats 42%
Memory: 16.46 MB beats 87%
Time taken: 45 minutes 11 seconds

I didn't use any hints or solutions. 
The first solution that came to mind was to use a trie structure. But I never used one before so I kept thinking of something else.
Then I considered backtracking: at each index i of s we consider to take any word from wordDict that starts with s[i].
Then we also need to consider spaces, but thats just index math.

============================================================================================================================================

catsanddog
i = 0, 'c'
We look for any words that have 'c' at position i (0)
Matches: "cat", "cats"

i = 1, 'a'
We look for any words (that we chose previously) that have 'a' at position i (1)
Matches: "cat", "cats"

i = 2, 't'
We look for any words (that we chose previously) that have 't' at position i (2)
Matches: "cat", "cats"

i = 3, 's'
We look for any words (that we chose previously) that have 's' at position i (3)
Only "cats" matches
But we also look for words that start with 's'
Matches: 'sand'

"""
from typing import List
def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    n = len(s)
    ans = []
    def backtrack(i, curr_sentence, len_last_added_word):
        if i == n:
            # Before we add curr_sentence to ans, we need to check that the last letters should be the same in s.
            # Check current sentence fits s
            for j in range(len_last_added_word):
                # Compare last letters (only) of s and curr_sentence
                if s[-1 -j] != curr_sentence[-2 -j]: # Skip last space in curr_sentence
                    return # Backtrack
            ans.append(curr_sentence)
            return # Done with decision
        
        # Check current sentence fits s, that means last letters of added word should be the same as s
        for j in range(len_last_added_word):
            # Compare last letters of curr_sentence and current index i of s
            # If curr_sentence has more letters than s, then we backtrack
            if i - 1 - j < 0 or len(s) <= i - 1 - j or s[i - 1 - j] != curr_sentence[-2 -j]: # Skip last space in curr_sentence
                return # Backtrack
        
        # Current sentence fits
        #print(i, curr_sentence, s[i])
        for word in wordDict:
            # If word starts with s[i]
            if word[0] == s[i]:
                #print(f"Word {word} starts with s[{i}] = {s[i]}")
                # Then we consider this word, we can increment i by length of word.
                backtrack(i+len(word), curr_sentence + word + " ", len(word))
    backtrack(0, "", 0)
    # Remove last spaces
    for i in range(len(ans)):
        ans[i] = ans[i][:-1]
    return ans

if __name__ == "__main__":
    res = wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
    for w in ["cats and dog","cat sand dog"]:
        assert w in res

    res = wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])
    for w in ["pine apple pen apple","pineapple pen apple","pine applepen apple"]:
        assert w in res
    
    assert wordBreak("catsandog", ["cats","dog","sand","and","cat"]) == []

    assert wordBreak("acccbccb", ["cc","bc","ac","ca"]) == []
