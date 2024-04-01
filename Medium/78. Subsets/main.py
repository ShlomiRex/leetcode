"""
Runtime: 35 ms beats 73%
Memory: 16 MB beats 31%
Time taken: 40 minutes
"""
from typing import List
def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    def backtrack(current_subset: List[int], candidates_start_index: int):
        res.append(current_subset)
        for i in range(candidates_start_index, len(nums)):
            backtrack(current_subset[:] + [nums[i]], i + 1)
    backtrack([], 0)
    return res

if __name__ == "__main__":
    assert subsets([1,2,3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    assert subsets([0]) == [[], [0]]
    
    