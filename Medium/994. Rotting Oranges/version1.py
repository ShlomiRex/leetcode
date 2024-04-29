"""
Runtime: 52 ms beats 46%
Memory: 16.6 MB beats 25%
Time taken: 30 minutes

BFS, count tree height
"""
from typing import List
def orangesRotting(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    visited = set() # Maybe use grid instead of visited set? less memory

    # First find rotten oranges
    queue = []
    oranges_count = 0 # Including rotten or non-rotten
    num_rotten_oranges = 0 # Only rotten oranges (grid = 2)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != 0:
                oranges_count += 1
            if grid[row][col] == 2:
                num_rotten_oranges += 1
                visited.add((row, col))
                queue.append((row, col+1))
                queue.append((row, col-1))
                queue.append((row+1, col))
                queue.append((row-1, col))
    # All oranges are 'rotten' we return 0 time is taken.
    if oranges_count == 0:
        return 0
    ans = -1
    while queue:
        #print(f"Queue: {queue}, visited: {visited}")
        ans += 1
        next_queue = []
        # Pop all queue
        for _ in range(len(queue)):
            row, col = queue.pop(0)
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != 1:
                continue
            if (row, col) not in visited:
                visited.add((row, col))
                grid[row][col] = 2 # This orange becomes rotten
                num_rotten_oranges += 1
                next_queue.append((row, col+1))
                next_queue.append((row, col-1))
                next_queue.append((row+1, col))
                next_queue.append((row-1, col))
        queue = next_queue

    if num_rotten_oranges != oranges_count:
        ans = -1
    return ans

if __name__ == "__main__":
    assert orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert orangesRotting([[0,2]]) == 0
    assert orangesRotting([[0]]) == 0
    