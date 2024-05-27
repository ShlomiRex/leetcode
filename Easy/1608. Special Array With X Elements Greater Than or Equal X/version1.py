"""
Runtime: 51 ms beats 15%
Memory: 16.7 MB beats 14%
Time taken: 10 minutes 25 secodns

Brute force solution.
"""
from typing import List
def specialArray(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    for x in range(n+1):
        count = 0
        for i in range(n):
            if nums[i] >= x:
                count += 1
        if count == x:
            return x
    return -1

if __name__ == "__main__":
    assert specialArray([3,5]) == 2
    assert specialArray([0,0]) == -1
    assert specialArray([0,4,3,0,4]) == 3