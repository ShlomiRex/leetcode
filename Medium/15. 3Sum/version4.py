"""
Runtime: 633 ms beats 78%
Memory: 20.7 MB beats 51%

I needed to see solutions of neetcode.
This is the correct answer.

Runtime complexity: O(n log n) + O(n^2) = O(n^2)
Memory complexity: O(1) or O(n) because we sort, depending on library, it can use memory.
"""
from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort() # O(n log n)
    ans = []

    for i, target in enumerate(nums):
        # Prevent duplicates by skipping iterating the same previous number
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # Two-sum II - Input is sorted array

        # Instead of l=0 we start l=i+1. Reason: to avoid reusing the current element
        l, r = i+1, len(nums) - 1
        while l < r:
            threeSum = target + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                ans.append([target, nums[l], nums[r]])
                l += 1 # In any case we increase left pointer, because if we do nothing, this is infinite loop.
                # But what happens if nums[l] == nums[l+1]? Then this is duplicate! We want to increase l until we reach non-duplicate
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return ans

if __name__ == "__main__":
    res = threeSum([-1,0,1,2,-1,-4])
    correct_answers = [[-1,-1,2],[-1,0,1]]
    for ans in correct_answers:
        assert ans in res

    res = threeSum([0,1,1])
    assert res == []

    res = threeSum([0,0,0])
    assert res == [[0,0,0]]