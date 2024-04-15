"""
Runtime: 40 ms beats 39%
Memory: 16.5 MB beats 64%
"""
from typing import List
def tictactoe(moves: List[List[int]]) -> str:
    board = [
        ['','',''],
        ['','',''],
        ['','','']
    ]

    curr_player = False # False = A, True = B

    # Play moves
    for move in moves:
        board[move[0]][move[1]] = 'X' if not curr_player else 'O'
        curr_player = not curr_player

    # Check winners
    # Check rows
    for row in board:
        if ''.join(row) in ["XXX", "OOO"]:
            return 'A' if row[0] == 'X' else 'B'
    
    # Check cols
    for col_index in range(3):
        col = [board[i][col_index] for i in range(3)]
        if ''.join(col) in ['XXX', 'OOO']:
            return 'A' if board[0][col_index] == 'X' else 'B'
    
    # Check main diagonal
    main_diagonal = [board[i][i] for i in range(3)]
    if ''.join(main_diagonal) in ['XXX', 'OOO']:
        return 'A' if board[0][0] == 'X' else 'B'
    
    # Check secondary diagonal
    secondary_diagonal = [board[i][2-i] for i in range(3)]
    if ''.join(secondary_diagonal) in ['XXX', 'OOO']:
        return 'A' if board[0][2] == 'X' else 'B'
    
    # Check draw
    return "Draw" if len(moves) == 9 else "Pending"

if __name__ == "__main__":
    assert tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]) == 'A'
    assert tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]) == 'B'
    assert tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]) == 'Draw'