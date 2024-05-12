"""
Runtime: 131 ms beats 53%
Memory: 17.1 MB beats 28%
Time taken: 8 minutes 38 seconds
"""
from typing import List
def largestLocal(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    maxLocal = [] # (n-2) x (n-2)

    def getAdjacencies(row, col):
        inds = [
            (row-1, col-1), (row-1, col), (row-1, col+1),
            (row, col-1), (row, col), (row, col+1),
            (row+1, col-1), (row+1, col), (row+1, col+1)
        ]
        adj = []
        for r, c in inds:
            if r >= 0 and c >= 0 and r < n and c < n:
                adj.append(grid[r][c])
        return adj
    for i in range(n-2):
        maxLocal.append([0]*(n-2))
        for j in range(n-2):
            maxLocal[i][j] = max(getAdjacencies(i+1, j+1))

    return maxLocal

if __name__ == "__main__":
    assert largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]) == [[9,9],[8,6]]
    assert largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]) == [[2,2,2],[2,2,2],[2,2,2]]