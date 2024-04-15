"""
Runtime: 44 ms beats 12%
Memory: 16.48 MB eats 94%

1. Play the moves
2. Keep track of the current player (A,B)
3. After all moves finished, we check board
4. We check for winner, if so, print the player that won (A or B)
5. If no, then we check if we get draw by checking length of moves == length of matrix
"""
from typing import List
def tictactoe(moves: List[List[int]]) -> str:
    board = [
        ['','',''],
        ['','',''],
        ['','','']
    ]

    curr_player = False # False = A, True = B
    for move in moves:
        row = move[0]
        col = move[1]
        board[row][col] = 'X' if not curr_player else 'O'
        curr_player = not curr_player

    # Check winners
    # Check rows
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and (row[2] == 'O' or row[2] == 'X'):
            x_or_o = row[0]
            player = 'A' if x_or_o == 'X' else 'B'
            return player
    
    # Check cols
    for col_index in range(3):
        if board[0][col_index] == board[1][col_index] and board[1][col_index] == board[2][col_index] and (board[0][col_index] == 'O' or board[0][col_index] == 'X'):
            x_or_o = board[0][col_index]
            player = 'A' if x_or_o == 'X' else 'B'
            return player
    
    # Check main diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and (board[0][0] == 'O' or board[0][0] == 'X'):
        x_or_o = board[0][0]
        player = 'A' if x_or_o == 'X' else 'B'
        return player
    
    # Check secondary diagonal
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and (board[0][2] == 'O' or board[0][2] == 'X'):
        x_or_o = board[0][2]
        player = 'A' if x_or_o == 'X' else 'B'
        return player
    
    # Check draw
    if len(moves) == 9:
        return "Draw"
    
    return "Pending"

if __name__ == "__main__":
    assert tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]) == 'A'
    assert tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]) == 'B'
    assert tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]) == 'Draw'