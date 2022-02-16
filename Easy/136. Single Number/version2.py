from typing import List
from operator import xor

"""
Runtime: 158 ms, faster than 63.69% of Python3 online submissions for Single Number.
Memory Usage: 16.4 MB, less than 96.71% of Python3 online submissions for Single Number.
"""

def singleNumber(nums: List[int]) -> int:

    if len(nums) == 1:
        return nums[0]

    cur_calculation = nums[0]

    for i in range(1, len(nums)):
        n = nums[i]
        cur_calculation = xor(n, cur_calculation)

    return cur_calculation


if __name__ == "__main__":
    nums = [2,2,1]
    res = singleNumber(nums)
    print(res)
    assert res == 1

    nums = [4,1,2,1,2]
    res = singleNumber(nums)
    print(res)
    assert res == 4

    nums = [1, 2, 2]
    res = singleNumber(nums)
    print(res)
    assert res == 1

    nums = [1]
    res = singleNumber(nums)
    print(res)
    assert res == 1

    nums = [2, 1, 5, 2, 1, 3, 3]
    res = singleNumber(nums)
    print(res)
    assert res == 5