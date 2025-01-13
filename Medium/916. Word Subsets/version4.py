"""
Time taken: 1:21:22
Runtime complexity: O(len(words1) + len(words2) + len(words1) * len(words2)) = O(len(words1) * len(words2)

The key point is instead of calculating freq dictionary for all subsets in words2, we calculate a single dictionary hashmap that will contain the maximum freq of all subsets in words2.

This way we avoid iterating over all words2 frequencies, we only iterate through one.
"""

from collections import defaultdict
from typing import Dict, List

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    res = []

    # Calculate freqs for words1
    candidate_freqs = []
    for candidate in words1:
        candidate_freq = defaultdict(int)
        for c in candidate: 
            candidate_freq[c] += 1
        candidate_freqs.append(candidate_freq)

    # Calculate freqs for words2
    # Here we can calculate MAXIMUM FREQ OF ALL SUBSETS TOGETHER
    # Thats how we deal with time limit exceeded
    subsets_freq = defaultdict(int)
    for subset in words2:
        subset_freq = defaultdict(int)
        for c in subset: 
            subset_freq[c] += 1
            subsets_freq[c] = max(subsets_freq[c], subset_freq[c])

    # Check which word in words1 is universal
    for i in range(len(words1)):
        candidate_freq = candidate_freqs[i]
        is_universal = True

        # Check subset_freq is less than candidate
        if len(subsets_freq) > len(candidate_freq):
            is_universal = False
        
        for c in subsets_freq:
            if c not in candidate_freq or candidate_freq[c] < subsets_freq[c]:
                is_universal = False
                break
        if is_universal: res.append(words1[i])
    return res
        
if __name__ == "__main__":
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","o"]
    res = wordSubsets(words1, words2)
    assert res == ["facebook","google","leetcode"]

    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["l","e"]
    res = wordSubsets(words1, words2)
    assert res == ["apple","google","leetcode"]

    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e"]
    res = wordSubsets(words1, words2)
    assert res == ["apple","facebook","google","leetcode"]

    words1 = ["amazon"]
    words2 = ["e"]
    res = wordSubsets(words1, words2)
    assert res == []

    words1 = ["google"]
    words2 = ["lo","eo"]
    res = wordSubsets(words1, words2)
    assert res == ["google"]
