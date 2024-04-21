"""
Runtime: 774 ms beats 85%
Memory: 31.15 MB beats 49%

Instead of DFS we use regular matrix for loops.
"""
from typing import List
def findFarmland(land: List[List[int]]) -> List[List[int]]:
    rows = len(land)
    cols = len(land[0])
    ans = []
    for row in range(rows):
        for col in range(cols):
            if land[row][col] == 1:
                min_row, min_col = row, col
                max_row, max_col = findBottomRightCorner(land, row, col)
                ans.append([min_row, min_col, max_row, max_col])
    return ans
def findBottomRightCorner(land, row, col) -> List[int]:
    rows = len(land)
    cols = len(land[0])

    # Find max_row, max_col of the group of farmland
    max_row, max_col = row, col
    for col_i in range(col, cols):
        if land[row][col_i] == 1:
            max_col = col_i
        else: break
    for row_i in range(row, rows):
        if land[row_i][col] == 1:
            max_row = row_i
        else: break
    # Fill entire farmland group wihh 0
    for row_i in range(row, max_row+1):
        for col_i in range(col, max_col+1):
            land[row_i][col_i] = 0
    
    return max_row, max_col

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