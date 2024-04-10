"""
Runtime: 49 ms beats 35%
Memory: 16.8 MB beats 80%
I did not code this. However my intuition was correct, I only didn't use queue to probe next available indecie.
"""
from collections import deque
from typing import List
def deckRevealedIncreasing(deck: List[int]) -> List[int]:
    l = len(deck)
    deck.sort()
    res = [0]*l
    available_indecies = deque(range(l))
    for sorted_card in deck:
        available_index = available_indecies.popleft()
        res[available_index] = sorted_card
        if available_indecies:
            available_indecies.append(available_indecies.popleft())
    return res
    

if __name__ == "__main__":
    # [2,13,3,11,5,17,7] -> 2
    # [3,11,5,17,7,13] -> 3
    # [5,17,7,13,11] -> 5
    # [7,13,11,17] -> 7
    # [11,17,13] -> 11
    # [13,17] -> 13
    # [17] -> 17
    # [] -> End
    assert deckRevealedIncreasing([17,13,11,2,3,5,7]) == [2,13,3,11,5,17,7]
