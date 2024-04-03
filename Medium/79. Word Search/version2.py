"""
Runtime: 3053 ms beats 86%
Memory: 16.58 MB beats 71%

Instead of 'visited' set, we can modify the board itself and mark visited cells. After calling the DFS function recursivly 4 times, we restore the board back.
This simple optimization decreased runtime by 2x.
"""
from typing import List
def exist(board: List[List[str]], word: str) -> bool:
    rows, cols, word_len = len(board), len(board[0]), len(word)

    if word_len > rows * cols:
        return False

    def dfs(row, col, word_index) -> bool:
        #print(f"Visited: {(row, col)}")
        if word_index == word_len:
            return True
        
        if (row < 0) or (col < 0) or (row >= rows) or (col >= cols) or board[row][col] != word[word_index]:
            #print("Going back")
            return False
        
        #print(f"Found word index: {word_index}, character: {word[word_index]}, location: {(row, col)}")

        temp = board[row][col] # Mark kcurrent cell as visited
        board[row][col] = ""

        if dfs(row, col+1, word_index+1) or dfs(row+1, col, word_index+1) or dfs(row-1, col, word_index+1) or dfs(row, col-1, word_index+1):
            return True

        board[row][col] = temp # Restore visited cell
        return False

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

if __name__ == "__main__":
    assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True
    assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE") == True
    assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") == False
    assert exist([["a", "a"]], "aa") == True
    assert exist([["a", "a"]], "aaa") == False
    assert exist([["a"]], "a") == True
    assert exist([["a"]], "b") == False
    assert exist([["a", "b"]], "ba") == True
    assert exist([["a", "b"]], "ab") == True
    assert exist([["a", "b"]], "aa") == False
    assert exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCEFSADEESE") == True