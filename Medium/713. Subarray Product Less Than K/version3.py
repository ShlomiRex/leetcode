"""

Runtime: 542 ms, beats 10%
Memory: 19.3 MB, beats 16%
Time it took to code: 1 hour, but the actual idea was like 1-2 minutes, the implementation was hard.

This is a solution that I looked for, so its not entirely mine, but I did come up with the actual idea fast.
"""
from typing import List
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    # This is exception case, if k is 0 or 1, then we can't have any subarray with product<k (less than 1).
    if k <= 1:
        return 0
    res, left,right, current_product = 0, 0, 0, 1
    while right < len(nums):
        current_product *= nums[right]
        # Only if is NOT (product<k) then we increase left window, until it is
        # We may need to remove multiple left elements if the product is too big (>=k).
        # This is why we use while loop.
        while current_product >= k:
            current_product /= nums[left]
            left += 1
        res += right - left + 1 # We add the length of the subarray that meets the condition product<k
        # We do this because if the subarray matches product<k, then any subarray without the first element will also match product<k, because each element is >1 so a subarray without the first element always shrinks the product of it.
        right += 1
    return res

if __name__ == "__main__":
    #assert numSubarrayProductLessThanK([10,5,2,6], 100) == 8
    assert numSubarrayProductLessThanK([1,2,3], 0) == 0
    assert numSubarrayProductLessThanK([1,1,1], 1) == 0
    assert numSubarrayProductLessThanK([1,1,1], 2) == 6
        