"""
Runtime: 127 ms beats 57%
Memory: 18.1 MB beats 78%
Time taken: 1 minute 57 seconds

Version 1 is better
"""
from typing import List
def moveZeroes(nums: List[int]) -> None:
    replace_ind = 0
    for num in nums:
        if num != 0:
            nums[replace_ind] = num
            replace_ind += 1
    for i in range(replace_ind, len(nums)):
        nums[i] = 0
    return nums

if __name__ == "__main__":
    assert moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]
    assert moveZeroes([0]) == [0]
    assert moveZeroes([1]) == [1]
    assert moveZeroes([2, 1]) == [2, 1]