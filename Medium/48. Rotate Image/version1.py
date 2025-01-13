"""
Runtime complexity: O(n * n) - each cell is rotated once exactly

Subproblem: only rotate the outer circle of a matrix
Keep doing this subproblem, go deeper into the [1,1] and [2,2] circles and so on to solve the bigger problem

Subproblem:

matrix[0][0] -> matrix[0][n-1] -> matrix[n-1][n-1] -> matrix[n-1][0] -> matrix[0][0]
where 0 is the outer circle, and n is the maximum row length at inner circle = 0

"""
from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    if n >= 3:
        # Inner circle only if n >= 3
        for inner_circle in range(len(matrix)-2):
            n = len(matrix) - inner_circle*2 # Because we have 2 less elements: one on right side, one on left side
            # print(f"inner_circle = {inner_circle}, n = {n}")
            for i in range(n-1):
                top_left = matrix[inner_circle][inner_circle + i] # (0,0), (1, 1), ... 
                top_right = matrix[inner_circle + i][n-1 + inner_circle]
                bottom_right = matrix[n-1 + inner_circle][n-1 - i + inner_circle]
                bottom_left = matrix[n-1 - i + inner_circle][inner_circle]

                # print(top_left, top_right, bottom_right, bottom_left)

                # Clock-wise rotation
                matrix[inner_circle][inner_circle + i] = bottom_left
                matrix[inner_circle + i][n-1 + inner_circle] = top_left
                matrix[n-1 + inner_circle][n-1 - i + inner_circle] = top_right
                matrix[n-1 - i + inner_circle][inner_circle] = bottom_right

                # print(matrix)
    elif n == 2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][1]
        d = matrix[1][0]
        matrix[0][0] = d
        matrix[0][1] = a
        matrix[1][1] = b
        matrix[1][0] = c
    else:
        # n == 1 or n == 0
        # do nothing
        pass
    
    
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    assert matrix == [[7,4,1],[8,5,2],[9,6,3]]

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(matrix)
    assert matrix == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    matrix = [1]
    rotate([1])
    assert matrix == [1]
