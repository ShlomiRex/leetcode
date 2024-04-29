"""
Runtime: 225 ms beats 71%
Memory: 19.5 MB beats 38%

We take brute force, and we see that we use previous calculations anyway, so why we don't store it and use it?
This is prefix sum. 

"""
from typing import List
from collections import defaultdict
def subarraySum(nums: List[int], k: int) -> int:
    ans = 0
    prefixSumFreq = defaultdict(int)
    prefixSumFreq[0] = 1 # The empty subarray is also valid (sum 0)
    _sum = 0
    for n in nums:
        _sum += n # We calculate cumulative sum
        if (_sum-k) in prefixSumFreq:
            ans += prefixSumFreq[_sum-k]
        prefixSumFreq[_sum] += 1
    return ans

if __name__ == "__main__":
    assert subarraySum([1,1,1], 2) == 2
    assert subarraySum([1,2,3], 3) == 2