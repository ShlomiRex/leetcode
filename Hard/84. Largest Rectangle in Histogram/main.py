"""
Runtime: 663 ms beats 63%
Memory: 33.3 MB beats 43%

Time complexity: O(n)
Memory complexity: O(n)
This is optimal.

Use monotonic stack. So as long as the heights are increasing, add them to the stack.
When we reach a height = heights[i] that is less than the top of the stack height, we reach critical point.
The stack helps us to keep left boundary of rectangle of each bar.
The element below the top of the stack is the last bar that was less than the current bar's height.

At this point, when the new bar is shorter than the bar corresponding to the index at the top of the stack,
it signifies a potential maximum width for the rectangle using the height of the bar at the stack's top.
This is because the new shorter bar establishes a new "right boundary" for the rectangles that can be formed
with all taller previous bars.
"""
from typing import List
def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack = [] # Keep pairs to index, height that represent the starting index of monotonic increasing heights
    for i, height in enumerate(heights):
        start = i
        # If we have elements in the stack and the top of the stack is monotonic increasing
        while stack and stack[-1][1] > height:
            stack_pop_index, stack_pop_height = stack.pop()
            maxArea = max(maxArea, stack_pop_height * (i - stack_pop_index)) # Height times width
            start = stack_pop_index
        stack.append((start, height))
    # If we still have elements left in stack we compute the areas
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights)-i))
    return maxArea

if __name__ == "__main__":
    assert largestRectangleArea([2,1,5,6,2,3]) == 10
    assert largestRectangleArea([2,4]) == 4