"""

Runtime: 924 ms beats 32%
Memory: 30 MB beats 56%
Time it took: 1 hour

"""
from typing import List

def countSubarrays(nums: List[int], k: int) -> int:
    num_good_subarrays, arr_max, l, r, freq = 0, max(nums), 0, 0, 0
    while r < len(nums):
        freq += 1 if nums[r] == arr_max else 0
        while freq >= k:
            num_good_subarrays += (len(nums) - r)
            freq -= 1 if nums[l] == arr_max else 0
            l += 1
        r += 1
    return num_good_subarrays


if __name__ == "__main__":
    assert countSubarrays([1,3,2,3,3], 2) == 6
    assert countSubarrays([1,4,2,1], 3) == 0