from typing import List


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
            push_to_end_of_array(i, nums)
            i = i - 1  # Because we swapped the element at index i with the last element of the array, the element at the current index is new
        else:
            k = k + 1
            cur_num = nums[i]
        i = i + 1
    return k


# Push element at index 'index' to the end of the array, which shifts all elements with index greater than 'index' to the left.
def push_to_end_of_array(index, arr):
    for i in range(index, len(arr) - 1):
        tmp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = tmp


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


