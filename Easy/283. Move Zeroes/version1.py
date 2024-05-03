from typing import List

def moveZeroes(nums: List[int]) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i], j = nums[i], nums[j], j+1

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    assert nums == [1,3,12,0,0]

    nums = [0]
    moveZeroes(nums)
    assert nums == [0]

    nums = [1]
    moveZeroes(nums)
    assert nums == [1]

    nums = [2, 1]
    moveZeroes(nums)
    assert nums == [2, 1]