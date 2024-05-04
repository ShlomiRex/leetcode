"""
Runtime: 358 ms beats 28%
Memory: 23.3 MB beats 66%
Time taken: 42 minutes, looked at solutions.


Minimum number of boats = maximum people per boat = find pairs of ppl 
that their weight is limit, if there is non, find the next best close weight.

Backtracking? We either take person i or don't, in the same boat. O(2^n)

We can count number of weights with hashmap or Counter.
Then sort by maximum weight.
Then we count number of pairs of people that can fit. 2 pointer maybe?

(Weight, Count)
[(3, 1), (2, 2), (1, 1)]

We start with largest: 3 = limit. Boats = 1
Then we got to 2. Its less than limit, so we need to find weight that is equal to 3-2=1. It does exist. Boats = 2
[(3, 0), (2, 1), (1, 0)]
Then we go to 2. We need to find weight of 3-2=1. We didn't find (because counter of 1 is 0). So this person is alone in the boat.
Boats = 3

Test case: [3,5,3,4], limit = 5
[(5, 1), (4, 1), (3, 2)]
We found weight=limit. Boats = 1

[(5, 0), (4, 1), (3, 2)]
We need to find weight of 5-4=1. We didn't found. So boats = 2.

[(5, 0), (4, 0), (3, 2)]
We need to find weight of 5-3=2. We didn't found. So boats = 3.

[(5, 0), (4, 0), (3, 1)]
We need to find weight of 5-3=2. We didn't found. So boats = 4.

In total boats = 4.
"""
from typing import List
def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    ans = 0
    l, r = 0, len(people)-1
    while l <= r:
        if people[l] + people[r] <= limit:
            r -= 1
            l += 1
        else:
            # Greater than. We need to ease up, so r -= 1
            r -= 1
        ans += 1
    return ans

if __name__ == "__main__":
    assert numRescueBoats(people = [1,2], limit = 3) == 1
    assert numRescueBoats(people = [3,2,2,1], limit = 3) == 3
    assert numRescueBoats(people = [3,5,3,4], limit = 5) == 4