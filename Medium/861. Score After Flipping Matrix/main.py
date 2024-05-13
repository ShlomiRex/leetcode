"""
Runtime: 52 ms beats 5%
Memory: 16 MB beats 59%
Time taken: 21 minutes 7 seconds

I did it alone, without help. No complex algorithm is needed. Only greedy approach.

Given row, how do you decide if to flip or not to flip?
First we calc the score for that row, then we flip the row and check the new score, if its greater then we keep it.
"""
from typing import List
def matrixScore(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    score = 0

    def calc_row_score(row):
        row_score = 0
        for col in range(n):
            row_score += grid[row][col] * (2 ** (n-1-col))
        return row_score

    def calc_row_score_flipped(row):
        row_score = 0
        for col in range(n):
            bit = 0 if grid[row][col] == 1 else 1
            row_score += bit * (2 ** (n-1-col))
        return row_score

    def flip_row(row):
        for col in range(n):
            bit = 0 if grid[row][col] == 1 else 1
            grid[row][col] = bit

    def flip_col(col):
        for row in range(m):
            bit = 0 if grid[row][col] == 1 else 1
            grid[row][col] = bit

    for row in range(m):
        score += calc_row_score(row)
    print(f"Score: {score}")
    
    # Decide if to flip rows
    for row in range(m):
        row_score = calc_row_score(row)
        row_score2 = calc_row_score_flipped(row)
        if row_score2 > row_score:
            flip_row(row)
    print(grid)

    # Decide if to flip cols
    for col in range(n):
        # Count number of 1's and 0's
        num_ones, num_zeros = 0, 0
        for row in range(m):
            if grid[row][col] == 1:
                num_ones += 1
            else:
                num_zeros += 1
        # flip col if more zeros than ones
        if num_zeros > num_ones:
            flip_col(col)
    
    # Calculate new score
    score2 = 0
    for row in range(m):
        score2 += calc_row_score(row)
    
    return max(score, score2)

if __name__ == "__main__":
    assert matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]) == 39
    assert matrixScore([[0]]) == 1
    