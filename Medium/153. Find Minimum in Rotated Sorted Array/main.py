"""
Runtime: 45 ms beats 42%
Memory: 16 MB beats 22%
Time taken: 11 min 39 seconds
"""
from typing import List
def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums)-1
    while l < r:
        m = (r + l)//2
        if nums[m] > nums[r]:
            l = m+1
        else:
            r = m
    return nums[l]

if __name__ == "__main__":
    assert findMin([3,4,5,1,2]) == 1
    assert findMin([4,5,6,7,0,1,2]) == 0
    assert findMin([11,13,15,17]) == 11
