"""
Runtime: 93 ms beats 97%
Memory: 17.6 MB beats 25%
"""
from typing import List
def twoSum(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers)-1
    while l < r:
        _sum = numbers[l] + numbers[r]
        if _sum > target: r -= 1
        elif _sum < target: l += 1
        else: return [l+1, r+1]

if __name__ == "__main__":
    assert twoSum(numbers = [2,7,11,15], target = 9) == [1,2]
    assert twoSum(numbers = [2,3,4], target = 6) == [1,3]
    assert twoSum(numbers = [-1,0], target = -1) == [1,2]
