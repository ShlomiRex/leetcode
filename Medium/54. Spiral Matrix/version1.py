"""
Runtime: 37 ms beats 45%
Memory: 16.6 MB beats 18%
Time taken: 18 minutes 28 seconds

Bad solution.
"""
from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    rows = len(matrix)
    cols = len(matrix[0])
    visited = set()
    ans = []
    row, col = 0, 0
    direction = 0 # 0 = right, 1 = down, 2 = left, 3 = up

    for _ in range(rows*cols):
        visited.add((row, col))
        curr_elem = matrix[row][col]
        ans.append(curr_elem)
        if direction == 0:
            # Right
            if col + 1 < cols and (row, col+1) not in visited:
                col += 1
            else:
                direction = (direction+1) % 4
                row += 1
        elif direction == 1:
            # Down
            if row + 1 < rows and (row+1, col) not in visited:
                row += 1
            else:
                direction = (direction+1) % 4
                col -= 1
        elif direction == 2:
            # Left
            if col -1 >= 0 and (row, col-1) not in visited:
                col -= 1
            else:
                direction = (direction+1) % 4
                row -= 1
        else:
            # Up
            if row - 1 >= 0 and (row-1, col) not in visited:
                row -= 1
            else:
                direction = (direction+1) % 4
                col += 1
    return ans

if __name__ == "__main__":
    assert spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
