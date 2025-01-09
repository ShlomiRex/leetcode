from typing import List

"""
Runtime: 867 ms, faster than 58.69% of Python3 online submissions for Maximum Subarray.
Memory Usage: 28 MB, less than 76.61% of Python3 online submissions for Maximum Subarray.
"""

def maxSubArray(nums: List[int]) -> int:
    max_sub_array_sum = nums[0]
    curr_sub_array_sum = 0
    for n in nums:
        curr_sub_array_sum = max(n, n + curr_sub_array_sum)
        max_sub_array_sum = max(max_sub_array_sum, curr_sub_array_sum)
    return max_sub_array_sum


if __name__ == "__main__":
    nums = [5, 4, -1, 7, 8]
    res = maxSubArray(nums)
    print(res)
    assert res == 23

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = maxSubArray(nums)
    print(res)
    assert res == 6

    nums = [1]
    res = maxSubArray(nums)
    print(res)
    assert res == 1

    nums = [1, 2]
    res = maxSubArray(nums)
    print(res)
    assert res == 3

    nums = [1, 2, -100, 100]
    res = maxSubArray(nums)
    print(res)
    assert res == 100

    nums = [1, 2, -1, 50]
    res = maxSubArray(nums)
    print(res)
    assert res == 52

    nums = [-1, -2, -3]
    res = maxSubArray(nums)
    print(res)
    assert res == -1




