from typing import List

"""
Time limit exceeded
"""

def maxSubArray(nums: List[int]) -> int:
    max_sub_array_sum = max(nums)

    for row in range(len(nums)):
        prev_sum = nums[row]
        for col in range(row + 1, len(nums)):
            cur_sum = prev_sum + nums[col]
            prev_sum = cur_sum
            max_sub_array_sum = max(max_sub_array_sum, cur_sum)

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




