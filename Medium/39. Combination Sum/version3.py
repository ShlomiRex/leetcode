"""
Brute force approach. Here we have duplicates.
For each node in our decision tree, we have all the candidates to pick from.
So its O(n^len(candidatees)) where n is number of decision nodes.
"""
from typing import List
def combinationSum(candidates: List[int], target: int):
    ans = []
    def backtrack(curr_array, curr_sum):
        if curr_sum > target:
            return
        if curr_sum == target:
            ans.append(curr_array)
        for i in range(len(candidates)):
            backtrack(curr_array[:] + [candidates[i]], curr_sum+candidates[i])
    backtrack([], 0)
    return ans


if __name__ == "__main__":
    res = combinationSum([2,3,6,7], 7)
    expected = [[2,2,3],[7]]
    for x in res:
        assert sorted(x) in sorted(expected)

    assert combinationSum([7], 7) == [[7]]
    res = combinationSum([2, 3, 5], 8)
    expected = [[2,2,2,2],[2,3,3],[3,5]]
    for x in res:
        assert sorted(x) in sorted(expected)
