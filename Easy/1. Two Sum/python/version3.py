"""
Runtime: 55 ms beats 81%
Memory: 17.7 MB beats 41%

We use single pass with hashmap.
"""

from collections import defaultdict
from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = defaultdict(int)
    for i, num in enumerate(nums):
        if (target-num) in hashmap and hashmap[(target-num)] != i: return [i, hashmap[(target-num)]]
        hashmap[num] = i


if __name__ == "__main__":
    assert set(twoSum([2, 7, 11, 15], 9)) == set([0, 1])
    assert set(twoSum([3, 2, 4], 6)) == set([1, 2])
    assert set(twoSum([3, 3], 6)) == set([0, 1])
    assert set(twoSum([2, 3, 3], 6)) == set([1, 2])
    assert set(twoSum([0, 0, 0, 0, 1, 1, 6, 0, 0], 6)) == set([3, 6])
    assert set(twoSum([6, -3], 3)) == set([0, 1])