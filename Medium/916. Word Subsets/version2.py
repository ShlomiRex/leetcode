"""
Time limit exceeded
45 / 56 testcases passed
"""

from collections import defaultdict
from typing import Dict, List

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:

    def is_hashmap_subset_of_another(subset: Dict[chr, int], hashmap: Dict[chr, int]) -> bool:
        # Check if subset hashmap is subset of hashmap (has all keys, and all values of subset are at most the values of hashmap)
        if len(subset.keys()) > len(hashmap.keys()):
            return False
        
        for subset_key in subset.keys():
            if subset_key not in hashmap or subset[subset_key] > hashmap[subset_key]: 
                return False
        return True

    res = []
    for a in words1:
        # Check universal
        char_count_hashmap = defaultdict(int)
        for c in a: char_count_hashmap[c] += 1
        #print(char_count_hashmap)

        # Check universal
        is_universal = True
        for b in words2:
            if len(b) > len(a): 
                is_universal = False
                break

            # Count chars in b
            subset_count_hashmap = defaultdict(int)
            for c in b: 
                subset_count_hashmap[c] += 1
                if c not in char_count_hashmap or subset_count_hashmap[c] > char_count_hashmap[c]:
                    is_universal = False
                    break

            is_subset = is_hashmap_subset_of_another(subset_count_hashmap, char_count_hashmap)
            #print(subset_count_hashmap, is_subset)

            if not is_subset:
                is_universal = False
                break
        if is_universal:
            res.append(a)
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
