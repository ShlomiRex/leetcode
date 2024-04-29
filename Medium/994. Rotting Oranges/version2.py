"""
Runtime: 47 ms beats 76%
Memory: 16.5 MB beats 65%

Time complexity: O(rows*cols) each cell is visited once
Space complexity: O(rows*cols) depends on queue, which can be all the matrix

Without using visited set. Also used queue.extend instead of 4 lines of python code.
"""
from typing import List
def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols, ans = len(grid), len(grid[0]), -1

    # First find rotten oranges
    queue, oranges_count, num_rotten_oranges = [], 0, 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != 0: oranges_count += 1
            if grid[row][col] == 2:
                num_rotten_oranges += 1
                queue.extend([(row, col+1), (row, col-1), (row+1, col), (row-1, col)])
    # All oranges are 'rotten' we return 0 time is taken.
    if oranges_count == 0: return 0
    while queue:
        #print(f"Queue: {queue}, visited: {visited}")
        ans, next_queue = ans+1, []
        # Pop all queue
        for _ in range(len(queue)):
            row, col = queue.pop(0)
            if row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == 1:
                grid[row][col] = 2 # This orange becomes rotten
                num_rotten_oranges += 1
                next_queue.extend([(row, col+1), (row, col-1), (row+1, col), (row-1, col)])
        queue = next_queue

    if num_rotten_oranges != oranges_count: ans = -1
    return ans

if __name__ == "__main__":
    assert orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert orangesRotting([[0,2]]) == 0
    assert orangesRotting([[0]]) == 0
    