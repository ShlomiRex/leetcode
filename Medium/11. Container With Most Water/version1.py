"""
Time taken: 25:24
Needed ChatGPT help why my code won't pass tests cases 31, 32

Runtime complexity: O(n) - optimal

============================================
Calculate container area: 
min(left_wall * right_wall) * (r - l)

Container with most water = we want to maximize both left, right walls
Two pointer approach

When we increase left pointer and when we decrease right pointer?

"""
from typing import List

def maxArea(height: List[int]) -> int:
    n = len(height)
    l, r = 0, n-1
    max_area = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area
            
if __name__ == "__main__":
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert maxArea([1,1]) == 1
    assert maxArea([3,6,1]) == 3
    assert maxArea([1,2,4,3]) == 4
