"""
Runtime: 156 ms beats 60%
Memory: 16.8 MB beats 85%
Time taken: 49 minutes 51 seconds
"""
from typing import List
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        click_row = click[0]
        click_col = click[1]
        clicked = board[click_row][click_col]
        # Rule 1
        if clicked == "M":
            # Game is over
            board[click_row][click_col] = 'X'
        elif clicked == 'E':
            self.rule2and3(board, click_row, click_col)
        return board
    
    def get_adjacent_ind(self, board, start_row, start_col):
        rows = len(board)
        cols = len(board[0])
        adj = [
            (start_row-1, start_col-1), (start_row-1, start_col), (start_row-1, start_col+1), 
            (start_row, start_col-1), (start_row, start_col+1), 
            (start_row+1, start_col-1), (start_row+1, start_col), (start_row+1, start_col+1), 
        ]
        return [(r, c) for r, c in adj if r >= 0 and c >= 0 and r < rows and c < cols]

    def rule2and3(self, board, click_row, click_col):
        queue = [(click_row, click_col)]
        while queue:
            r, c = queue.pop(0)
            if board[r][c] != 'E':
                continue
            board[r][c] = 'B'
            adjacent_cells = self.get_adjacent_ind(board, r, c)
            num_adj_mines = 0
            for adj_r, adj_c in adjacent_cells:
                if board[adj_r][adj_c] == 'M':
                    num_adj_mines += 1
            if num_adj_mines > 0:
                board[r][c] = str(num_adj_mines)
            else:
                for adj_r, adj_c in adjacent_cells:
                    queue.append((adj_r, adj_c))


if __name__ == "__main__":
    board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
    click = [3,0]
    assert Solution().updateBoard(board, click) == [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

    board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
    click = [1,2]
    assert Solution().updateBoard(board, click) == [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]