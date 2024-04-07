"""
Runtime: 4082 ms beats 5%
Memory: 28 MB beats 13%

A group of anagrams is a group of strings, such that the all the strings in that group, have the same length and same characters frequency.

For each string, count frequency of words.
Now we check if that string should be in any anagram group we have so far. If not, create new anagram group.
If the string should be in an existing anagram group, add it to the group.
"""
from typing import List
from collections import defaultdict
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups = []

    def find_anagram_group(freq, freq_len):
        for anagram_group in anagram_groups:
            if int(anagram_group["len"]) == freq_len:
                # Check all characters have the same frequency
                all_freq_same = True
                anagram_freq = anagram_group["freq"]
                for c in anagram_freq:
                    if freq[c] != anagram_freq[c]:
                        all_freq_same = False
                        break
                if all_freq_same:
                    return anagram_group
        return None

    for s in strs:
        # Count freq
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        freq_len = len(freq)
        anagram_group = find_anagram_group(freq, freq_len)

        if anagram_group: # If found, add the current string to the group
            anagram_group["strings"].append(s)
        else: # Didn't find anagram group. This string creates new anagram group.
            anagram_groups.append({"freq": freq, "strings": [s], "len": freq_len})
    
    # Collect strings from each group
    res = []
    for group in anagram_groups:
        res.append(group["strings"])
    return res

if __name__ == "__main__":
    #assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(groupAnagrams(["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]))
    assert groupAnagrams(["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]) == [["tittt","tttit","tttti"],["hhhhu","hhhuh","hhuhh"]]