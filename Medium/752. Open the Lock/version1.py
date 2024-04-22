"""
Runtime: 1653 ms beats 8.1%
Memory: 19.3 MB beats 6%
Time taken: 51 minutes 16 seconds, and I looked up hints, but didn't look directly at the solution first. I had to fix order of lock digits.


Put dead ends in hashtable/hashset so its easier to find
Instead of starting at 0000 we start at target and we try to reach 0000
"""
from typing import List
def openLock(deadends: List[str], target: str) -> int:
    deadends = set(deadends)
    queue = [([0,0,0,0], 0)] # Current digits and wheel turns to get here
    visited = set()
    while queue:
        lock, moves = queue.pop(0)
        # Convert array of size 4 of ints to string ([0,0,0,0] -> "0000")
        str_lock = "".join(str(x) for x in lock)

        if str_lock in deadends or str_lock in visited: continue

        visited.add(str_lock)

        if str_lock == target: 
            return moves

        # We can move one of each dial up or down

        # First digit
        queue.append(([lock[0], lock[1], lock[2], ((lock[3]+1) % 10)], moves+1))
        queue.append(([lock[0], lock[1], lock[2], ((lock[3]-1) % 10)], moves+1))

        # Second digit
        queue.append(([lock[0], lock[1], ((lock[2]+1) % 10), lock[3]], moves+1))
        queue.append(([lock[0], lock[1], ((lock[2]-1) % 10), lock[3]], moves+1))

        # Third digit
        queue.append(([lock[0], ((lock[1]+1) % 10), lock[2], lock[3]], moves+1))
        queue.append(([lock[0], ((lock[1]-1) % 10), lock[2], lock[3]], moves+1))

        # Fourth digit
        queue.append(([((lock[0]+1) % 10), lock[1], lock[2], lock[3]], moves+1))
        queue.append(([((lock[0]-1) % 10), lock[1], lock[2], lock[3]], moves+1))

    return -1

if __name__ == "__main__":
    assert openLock(["0201","0101","0102","1212","2002"], target="0202") == 6
    assert openLock(["8888"], target = "0009") == 1
    assert openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888") == -1