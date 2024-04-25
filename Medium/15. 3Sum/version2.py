"""
Almost correct answer. This solution contains duplicates, however.
"""
from collections import defaultdict
from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort() # O(n log n)
    ans = []

    # This is 1-indexed.
    def twoSumII(target, target_ind):
        l, r = 0, len(nums)-1
        while l < r:
            _sum = nums[l] + nums[r]
            if _sum > target: r -= 1
            elif _sum < target: l += 1
            else: return [l+1, r+1]
        return None

    for i, target in enumerate(nums):
        # Two-sum II - Input is sorted array
        tmp = twoSumII(-target, i)
        if tmp:
            ind1, ind2 = tmp
            ind1 -= 1
            ind2 -= 1
            print(f"Adding: {[target, nums[ind1], nums[ind2]]}")
            ans.append([target, nums[ind1], nums[ind2]])

    return ans

if __name__ == "__main__":
    res = threeSum([-1,0,1,2,-1,-4])
    correct_answers = [[-1,-1,2],[-1,0,1]]
    for ans in correct_answers:
        assert ans in res


    res = threeSum([0,1,1])
    assert res == []

    res = threeSum([0,0,0])
    print(res)
    assert res == [[0,0,0]]