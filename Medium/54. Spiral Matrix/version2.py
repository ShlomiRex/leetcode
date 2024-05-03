"""
Runtime: 37 ms beats 45%
Memory: 16.4 MB beats 94%

Not my solution. But its better.
"""
from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows-1, 0, cols-1
    result = []
    
    while len(result) < rows * cols:
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1
        
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

if __name__ == "__main__":

    assert spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
