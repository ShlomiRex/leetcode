"""
Time taken: 51:24

I broke my head trying to achieve O(n) time and O(1) space.
O(1) space can't be done. This is O(n) space.
"""
from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    l, r = 0, n - 1
    i = n - 1
    res = [0] * n

    while l <= r and l < n and r > -1:
        left = nums[l] ** 2
        right = nums[r] ** 2
        if right >= left:
            res[i] = right
            i -= 1
            r -= 1
        else:
            # left > right
            res[i] = left
            i -= 1
            l += 1

    return res

if __name__ == "__main__":
    assert sortedSquares([-4,-1,0,3,10]) == [0, 1, 9, 16, 100]
    assert sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
    assert sortedSquares([-4, -1, 2, 10]) == [1, 4, 16, 100]