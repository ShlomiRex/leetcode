from typing import List


def removeElement(nums: List[int], val: int) -> int:
    i,j = 0, 0
    while j < len(nums):
        if i == j:
            if nums[i] != val:
                i, j = i+1, j+1
            else:
                j += 1
        else:
            if nums[j] == val:
                j += 1
            else:
                nums[i] = nums[j]
                nums[j] = val
                i, j = i+1, j+1
    return i

if __name__ == "__main__":
    nums = [3,2,2,3]
    assert removeElement(nums, 3) == 2

    nums = [0,1,2,2,3,0,4,2]
    assert removeElement(nums, 2) == 5

    nums = [0,1,2,2,3,0,4,2]
    assert removeElement(nums, 2) == 5
