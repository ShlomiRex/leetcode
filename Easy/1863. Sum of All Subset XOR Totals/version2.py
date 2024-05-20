"""
Runtime: 54 ms beats 55%
Memory: 16.6 MB beats 33%

Huge performance boost where subsets recursion we give XOR total instead of curr_subset
Notice, we return xor_with_numsi and xor_without_numsi 
"""
from typing import List
def subsetXORSum(nums: List[int]) -> int:
    n = len(nums)
    def subsets(curr_xor, i):
        if i == n:
            return curr_xor
        xor_with_numsi = subsets(curr_xor^nums[i], i+1)
        xor_without_numsi = subsets(curr_xor, i+1)
        return xor_with_numsi + xor_without_numsi
    return subsets(0, 0)

if __name__ == "__main__":
    assert subsetXORSum([1, 3]) == 6
    # assert subsetXORSum([5,1,6]) == 28
    # assert subsetXORSum([3,4,5,6,7,8]) == 480