"""
Runtime: 58 ms beats 30%
Memory: 16.5 MB beats 94%
Time taken: 33 minutes 51 seconds, although I loooked at other solutions.


========================================================================================================================
Very simillar to previous day question backtracking: 2597. The Number of Beautiful Subsets


Decision: at each word we either skip the current word, or we include it.
We keep track of current score
Backtrack: when current word requires more letters than we have in counter, we backtrack
Goal: reach end of list of words.
"""
from typing import List
from collections import Counter
def maxScoreWords(words: List[str], letters: List[str], score: List[int]) -> int:
    n = len(words)

    def backtrack(i, counter):
        if i == n:
            return 0 # We reached end. The max score of 'Nothing' is 0.

        # Skip current word, counter stays the same
        best = backtrack(i + 1, counter)

        # Take current word only if valid
        # We check (Counter > Counter) [counter of words[i] and counter of letters] which is valid python evaluation
        # It means we can fit f into counter (so counter has enough letters)
        f = Counter(words[i])
        if counter > f:
            # Calc score of word
            word_score = 0
            for c in words[i]: 
                word_score += score[ord(c) - ord('a')]
            # One liner: score[ord(c) - ord('a')] for c in words[i]
            counter -= f # Decrease counter by amount of letters in word[i]
            best = max(best, backtrack(i + 1, counter) + word_score)
            counter += f
        return best
    # Consider first word (index 0) with all letters available
    return backtrack(0, Counter(letters))

if __name__ == "__main__":
    words = ["dog","cat","dad","good"]
    letters = ["a","a","c","d","d","d","g","o","o"]
    score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    assert maxScoreWords(words, letters, score) == 23

    words = ["xxxz","ax","bx","cx"]
    letters = ["z","a","b","c","x","x","x"]
    score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
    assert maxScoreWords(words, letters, score) == 27

    words = ["leetcode"]
    letters = ["l","e","t","c","o","d"]
    score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
    assert maxScoreWords(words, letters, score) == 0
