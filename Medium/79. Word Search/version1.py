"""
Runtime: 6706 ms beats 11%
Memory: 16.59 MB beats 71%
Time taken: 2 hours
"""
from typing import List
def exist(board: List[List[str]], word: str) -> bool:
    rows, cols, word_len = len(board), len(board[0]), len(word)

    if word_len > rows * cols:
        return False

    def dfs(row, col, word_index, visited) -> bool:
        #print(f"Visited: {(row, col)}")
        if (row < 0) or (col < 0) or (row >= rows) or (col >= cols) or ((row, col) in visited):
            #print("Going back")
            return False
        if word_index == word_len:
            return True
        if board[row][col] == word[word_index]:
            if word_index == word_len - 1:
                return True
            visited.add((row, col))
            #print(f"Found word index: {word_index}, character: {word[word_index]}, location: {(row, col)}")
            return dfs(row, col+1, word_index+1, visited.copy()) or dfs(row+1, col, word_index+1, visited.copy()) or dfs(row-1, col, word_index+1, visited.copy()) or dfs(row, col-1, word_index+1, visited.copy())
        #print("Going back")
        return False

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0, set()):
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