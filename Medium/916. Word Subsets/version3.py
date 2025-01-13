"""
Still time limit exceeded
45 / 56 testcases passed
"""

from collections import defaultdict
from typing import Dict, List

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    res = []
    for candidate in words1:
        is_universal = True

        candidate_freq = defaultdict(int)
        for c in candidate: candidate_freq[c] += 1

        for subset in words2:
            subset_freq = defaultdict(int)
            for c in subset: subset_freq[c] += 1

            # Check candidate_freq is less than subset_freq
            if len(subset_freq) > len(candidate_freq):
                is_universal = False
                break
            
            for c in subset_freq:
                if c not in candidate_freq or candidate_freq[c] < subset_freq[c]:
                    is_universal = False
                    break
        

        if is_universal: res.append(candidate)
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
