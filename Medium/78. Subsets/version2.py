"""
Runtime: 34 ms beats 77%
Memory: 16.6 MB beats 77%

Solution taken from neetcode.
"""
from typing import List
def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        # Include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # Don't include nums[i]
        subset.pop()
        dfs(i+1)

    dfs(0)
    return res


if __name__ == "__main__":
    ans = subsets([1,2,3])
    for x in [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]:
        assert x in ans

    ans = subsets([0])
    for x in [[], [0]]:
        assert x in ans

    
    