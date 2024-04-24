"""
Runtime: 115 ms beats 13%
Memory: 17.5 MB beats 25%
Time taken: 7 minutes 23 seconds

We use two-pointer approach, which is constant space and O(n) runtime complexity.
"""
from typing import List
def twoSum(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    l, r = 0, n-1
    while l < r:
        _sum = numbers[l] + numbers[r]
        if _sum > target:
            r -= 1
        elif _sum < target:
            l += 1
        else:
            return [l+1, r+1]

if __name__ == "__main__":
    assert twoSum(numbers = [2,7,11,15], target = 9) == [1,2]
    assert twoSum(numbers = [2,3,4], target = 6) == [1,3]
    assert twoSum(numbers = [-1,0], target = -1) == [1,2]
