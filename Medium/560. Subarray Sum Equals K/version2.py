"""

"""
from typing import List
def subarraySum(nums: List[int], k: int) -> int:
    ans, n = 0, len(nums)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == k:
                ans += 1
    return ans

if __name__ == "__main__":
    assert subarraySum([1,1,1], 2) == 2
    assert subarraySum([1,2,3], 3) == 2