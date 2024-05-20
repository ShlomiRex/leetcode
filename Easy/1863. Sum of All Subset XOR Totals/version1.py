"""
Runtime: 208 ms beats 5%
Memory: 21.5 MB beats 7%
Time taken: 14 minutes 8 seconds

Stupid solution without optimization
"""
from typing import List
def subsetXORSum(nums: List[int]) -> int:
    n = len(nums)
    _subsets = []
    def subsets(curr_subset, i):
        if i == n:
            _subsets.append(curr_subset)
            return
        subsets(curr_subset[:]+[nums[i]], i+1)
        subsets(curr_subset[:], i+1)
    subsets([], 0)
    #print(_subsets)
    ans = 0
    for subset in _subsets:
        #print(f"Curr subset: {subset}")
        n2 = len(subset)
        if n2 == 1:
            #print(f"XOR total: {subset[0]}")
            ans += subset[0]
        elif n2 > 1:
            curr_xor = subset[0]
            for i in range(1, len(subset)):
                curr_xor ^= subset[i]
            #print(f"XOR total: {curr_xor}")
            ans += curr_xor
    return ans

if __name__ == "__main__":
    assert subsetXORSum([1, 3]) == 6
    assert subsetXORSum([5,1,6]) == 28
    assert subsetXORSum([3,4,5,6,7,8]) == 480