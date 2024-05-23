"""
Runtime: 4275 ms beats 23%
Memory: 16.58 MB beats 84%

I looked at solutions.

Decision tree: at each index, we either take the nums[i] or skip it, in order to get all subsets.
We need to keep track of numbers that we chosen so far.
If there exists a number such that (nums[index] - k == 0) or (nums[index] + k == 0) (which is equivelemnt to absolute difference), that means this subset isn't beatiful.
The counter will count the frequency of each element in current subset.
The counter helps us identify if this subset is beatiful by checking if there exists a number X such that | nums[index] - X | == k. This lookup is O(1), because counter is hashmap.

The result is stored in 'total' - in which we count number of subsets that are beatiful.
The recursion stops when we reach final index, where we can't add anymore nums[index] so we return 1, since its beatiful (if it wasn't beatiful we would fail on the if statement).

"""
from typing import List
from collections import Counter
def beautifulSubsets(nums: List[int], k: int) -> int:
    N = len(nums)

    def recurse(index, counter):
        if index == N:
            return 1
        
        total = 0
        # Skip nums[index], don't change counter
        total += recurse(index + 1, counter)

        # Check if beatiful |nums[index] - k| == 0
        # Take nums[index] if beatiful, update counter
        if counter[nums[index] - k] == 0 and counter[nums[index] + k] == 0:
            counter[nums[index]] += 1
            total += recurse(index + 1, counter)
            counter[nums[index]] -= 1
        return total

    return recurse(0, Counter()) - 1 # Remove empty set, its also beatiful but we don't care about it

if __name__ == "__main__":
    assert beautifulSubsets([2,4,6], 2) == 4
    assert beautifulSubsets([1], 1) == 1
    assert beautifulSubsets([], 1) == 0