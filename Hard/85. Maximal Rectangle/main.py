"""
Runtime: 212 ms beats 81%
Memory: 17.7 MB beats 97%

Very very hard problem. I attempted to solve this like in "Medium/200. Number of Islands" but the hard part is checking that an island is rectangle. Very very hard.

We use the same trick in "Hard/84. Largest Rectangle in Histogram".
We use stack to keep track of left boundary, and the stack is monotonically increasing, until we reach a bar/height that is less than the top of the stack.
Then we calculate width based on popping the stack, checking height, until we reach height less than current height.
"""
from typing import List
def maximalRectangle(matrix: List[List[str]]) -> int:
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * (cols + 1)  # Include an extra element for easier calculation
    max_area = 0
    
    for row in matrix:
        for i in range(cols):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        
        # Calculate max area using histogram method
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
    
    return max_area  

if __name__ == "__main__":
    assert maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 6
    assert maximalRectangle([["0"]]) == 0
    assert maximalRectangle([["1"]]) == 1