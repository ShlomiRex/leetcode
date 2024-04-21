"""
Runtime: 784 ms beats 81.5%
Memory: 31.07 MB beats 51%
"""
from typing import List
def findFarmland(land: List[List[int]]) -> List[List[int]]:
    rows, cols, ans = len(land), len(land[0]), []
    for row in range(rows):
        for col in range(cols):
            if land[row][col] == 1:
                max_row, max_col = findBottomRightCorner(land, row, col)
                ans.append([row, col, max_row, max_col])
    return ans
def findBottomRightCorner(land, row, col) -> List[int]:
    rows = len(land)
    cols = len(land[0])

    # Find max_row, max_col of the group of farmland
    max_row, max_col = row, col

    # Find max col
    while max_col < cols and land[row][max_col] == 1:
        max_col += 1
    
    # Find max row
    while max_row < rows and land[max_row][col] == 1:
        max_row += 1

    # Fill entire farmland group wihh 0
    for row_i in range(row, max_row):
        for col_i in range(col, max_col):
            land[row_i][col_i] = 0
    
    return max_row-1, max_col-1

if __name__ == "__main__":
    res = findFarmland([[1,0,0],[0,1,1],[0,1,1]])
    assert [0,0,0,0] in res
    assert [1,1,2,2] in res
    assert len(res) == 2

    res = findFarmland([[1,1],[1,1]])
    assert [0,0,1,1] in res
    assert len(res) == 1

    assert findFarmland([[0]]) == []

    res = findFarmland([[1,1],[0,0]])
    assert res == [[0,0,0,1]]