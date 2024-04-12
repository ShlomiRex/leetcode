"""
Runtime: 113 ms beats 27%
Memory: 18.5 MB beats 39%
"""
from typing import List
def trap(height: List[int]) -> int:
    n = len(height)
    maxLeftArr = [0] * n
    maxRightArr = [0] * n
    currMaxLeft, currMaxRight = 0, 0
    for i in range(n):
        maxLeftArr[i] = currMaxLeft
        currMaxLeft = max(currMaxLeft, height[i])
        maxRightArr[n-1-i] = currMaxRight
        currMaxRight = max(currMaxRight, height[n-1-i])
    # Calculate trappable water
    res = 0
    for i in range(n):
        water =  min(maxLeftArr[i], maxRightArr[i]) - height[i]
        if water > 0:
            res += water
    return res
        

if __name__ == "__main__":
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,2,0,3,2,5]) == 9