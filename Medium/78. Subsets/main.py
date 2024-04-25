"""
Runtime: 35 ms beats 73%
Memory: 16 MB beats 31%
Time taken: 40 minutes

Explanation: similar to BFS, the candidate_start_index is the tree height.
We start with [], 0 and do for loop, we get:

backtrack([1], 1)
backtrack([2], 1)
backtrack([3], 1)

This is the first loop. Now we enter [1],1, the loop will look like this:
backtrack([1,2], 2)
backtrack([1,3], 2)

Similarly, we enter [1,2], 1 is:
backtrack([1,2,3], 3)
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
    
    