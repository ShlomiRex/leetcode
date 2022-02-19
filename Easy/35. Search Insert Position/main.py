from typing import List

"""
Runtime: 77 ms, faster than 36.72% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.8 MB, less than 64.00% of Python3 online submissions for Search Insert Position.
"""

def searchInsert(nums: List[int], target: int) -> int:
    start_i = 0
    end_i = len(nums) - 1
    while start_i <= end_i:
        mid = (end_i + start_i) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            end_i = mid - 1
        else:
            start_i = mid + 1
    return start_i

if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    res = searchInsert(nums, target)
    print(res)
    assert res == 2

    nums = [1, 3, 5, 6]
    target = 2
    res = searchInsert(nums, target)
    print(res)
    assert res == 1

    nums = [1, 3, 5, 6]
    target = 7
    res = searchInsert(nums, target)
    print(res)
    assert res == 4

    nums = [2]
    target = 1
    res = searchInsert(nums, target)
    print(res)
    assert res == 0

    nums = [1]
    target = 2
    res = searchInsert(nums, target)
    print(res)
    assert res == 1

    nums = [1]
    target = 1
    res = searchInsert(nums, target)
    print(res)
    assert res == 0
