"""
Runtime: 56 ms beats 42%
Memory: 16.7 MB beats 15%

We take brute force approach and instead of having all the candidates to consider, we only consider 
candidates that have have no duplicates.
"""
from typing import List
def combinationSum(candidates: List[int], target: int):
    ans = []
    def backtrack(candidates_begin_index, curr_array, curr_sum):
        if curr_sum > target: return
        if curr_sum == target: ans.append(curr_array)
        for i in range(candidates_begin_index, len(candidates)): backtrack(i, curr_array[:] + [candidates[i]], curr_sum+candidates[i])
    backtrack(0, [], 0)
    return ans


if __name__ == "__main__":
    assert combinationSum([2,3,6,7], 7) == [[2,2,3],[7]]
    assert combinationSum([7], 7) == [[7]]
    assert combinationSum([2, 3, 5], 8) == [[2,2,2,2],[2,3,3],[3,5]]
    assert combinationSum([8,7,4,3], 11) == [[8,3],[7,4],[4,4,3]]

