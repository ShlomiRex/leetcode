"""
Runtime: 1185 ms beats 5% (really bad)
Memory: 30.29 MB beats 69%
Time taken: 23 minutes, took some time to fix small issues but the overall intuition was DFS
"""
from typing import List
def findFarmland(land: List[List[int]]) -> List[List[int]]:
    rows = len(land)
    cols = len(land[0])
    ans = []
    for row in range(rows):
        for col in range(cols):
            if land[row][col] == 1:
                group = findPlot(land, row, col)
                ans.append(group)
    return ans
def findPlot(land, row, col) -> List[int]:
    # Return top-left corner of farmland and bottom-right corner
    if row >= len(land) or col >= len(land[0]) or row < 0 or col < 0 or land[row][col] != 1:
        return [float('inf'), float('inf'), -1, -1]
    
    # Mark current cell as visited
    land[row][col] = 0

    # DFS
    res1 = findPlot(land, row, col+1)
    res2 = findPlot(land, row, col+1)
    res3 = findPlot(land, row-1, col)
    res4 = findPlot(land, row+1, col)

    min_row = min(res1[0], res2[0], res3[0], res4[0], row)
    min_col = min(res1[1], res2[1], res3[1], res4[1], col)
    max_row = max(res1[2], res2[2], res3[2], res4[2], row)
    max_col = max(res1[3], res2[3], res3[3], res4[3], col)
    
    return [min_row, min_col, max_row, max_col]

if __name__ == "__main__":
    res = findFarmland([[1,0,0],[0,1,1],[0,1,1]])
    assert [0,0,0,0] in res
    assert [1,1,2,2] in res
    assert len(res) == 2

    res = findFarmland([[1,1],[1,1]])
    assert [0,0,1,1] in res
    assert len(res) == 1

    assert findFarmland([[0]]) == []