from typing import List

"""
Runtime: 222 ms, faster than 10.94% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 78.57% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""

# Do not allocate extra space for another array.
# Complexity: O(n^2)
def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 1:
        return 1

    # Sorted array, check if last element is equal to first, then we do nothing.
    if nums[0] == nums[-1]:
        return 1

    k = 1
    cur_num = nums[0]

    i = 1
    for _ in range(1, len(nums)):
        if nums[i] == cur_num:
            # Push to tail
            nums.append(nums[i])
            # Remove the element
            nums.pop(i - 1)  # Because we pushed element at the tail, the length increased by 1. So we compoensate by decreasing by 1 the index.
            i = i - 1  # Because we swapped the element at index i with the last element of the array, the element at the current index is new
        else:
            k = k + 1
            cur_num = nums[i]
        i = i + 1
    return k



if __name__ == "__main__":
    nums = [1, 1, 1, 3]
    print(nums)
    res = removeDuplicates(nums)
    print(nums, "k =", res)
    assert res == 2

    nums = [1,1,2]
    print(nums)
    res = removeDuplicates(nums)
    print(nums, "k =", res)
    assert res == 2

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(nums)
    res = removeDuplicates(nums)
    print(nums, "k =", res)
    assert res == 5

    nums = [1, 2]
    print(nums)
    res = removeDuplicates(nums)
    print(nums, "k =", res)
    assert res == 2

    nums = [1, 1]
    print(nums)
    res = removeDuplicates(nums)
    print(nums, "k =", res)
    assert res == 1


