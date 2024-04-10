"""
Runtime: 49 ms beats 44%
Memory: 16.5 MB beats 51%
Time taken: 13 minutes

tickets[i] = number of tickets that the i'th person would like to buy

Brute force: iterate over array while tickets[i] != 0
    Add to time each tickets[i] that is not 0.
    Continue until tickets[i] == 0.
Return time.
"""
from typing import List
def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    time = 0
    i = 0
    while tickets[k] != 0:
        if tickets[i] > 0:
            tickets[i] -= 1
            time += 1
        i += 1
        if i == len(tickets):
            i = 0
    return time

if __name__ == "__main__":
    assert timeRequiredToBuy([2,3,2], 2) == 6
    assert timeRequiredToBuy([5,1,1,1], 0) == 8