"""
Runtime: 115 ms beats 23%
Memory: 18.6 MB beats 16.5%

I used hintes. Its hard.
Subproblem: the amount of water we can trap at each step i is determined by maximum height on left and maximum height on the right (i.e. less than i and greater than i)
So amount of water we can trap at each step is:
height[i] - min(maxLeft, maxRight)

where height[i] is the height at position i.
"""
from typing import List
def trap(height: List[int]) -> int:
    n = len(height)
    if n == 0:
        return 0
    maxLeftArr = [0] * n
    maxRightArr = [0] * n

    # Calculate maximum left, right arrays
    currMaxLeft, currMaxRight = 0, 0
    for i in range(n):
        maxLeftArr[i] = currMaxLeft
        currMaxLeft = max(currMaxLeft, height[i])
    for i in range(n-1, -1, -1):
        maxRightArr[i] = currMaxRight
        currMaxRight = max(currMaxRight, height[i])
    
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