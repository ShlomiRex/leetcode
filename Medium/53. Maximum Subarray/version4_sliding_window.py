from typing import List

"""
Time: 23:47
Runtime complexity: O(n) because we either move r right or l right one at a time, so technically its O(2n)

Used sliding window approach instead of Kadane's algorithm, solved alone

Brute force: calculate all sums of subarrays and return the maximum. O(n^2) time

Sliding window:
We either increase the right side or decrease the left side, depending if that number will make the current subarray sum bigger.

A single number can also be bigger than the current sum.
"""
def maxSubArray(nums: List[int]) -> int:
    n = len(nums)
    l, r = 0, 0
    max_sub_array = nums[0]
    curr_subarray_sum = 0

    while r < n and l < n:
        curr_subarray_sum += nums[r]
        
        # If a single number is bigger than the current sum
        if nums[r] > curr_subarray_sum:
            curr_subarray_sum = nums[r]
            l = r
        
        # Check if we have new max sum
        if curr_subarray_sum > max_sub_array:
            max_sub_array = curr_subarray_sum
        
        if r < n:
            r += 1
        else:
            curr_subarray_sum -= nums[l]
            l += 1
    return max_sub_array

if __name__ == "__main__":
    nums = [5, 4, -1, 7, 8]
    res = maxSubArray(nums)
    assert res == 23

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = maxSubArray(nums)
    assert res == 6

    nums = [1]
    res = maxSubArray(nums)
    assert res == 1

    nums = [1, 2]
    res = maxSubArray(nums)
    assert res == 3

    nums = [1, 2, -100, 100]
    res = maxSubArray(nums)
    assert res == 100

    nums = [1, 2, -1, 50]
    res = maxSubArray(nums)
    assert res == 52

    nums = [-1, -2, -3]
    res = maxSubArray(nums)
    assert res == -1




