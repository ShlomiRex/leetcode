"""
Runtime: 35 ms beats 85%
Memory: 16.61 MB beats 14%

Prefix sum solution. Taken from editorial.
"""
from typing import List
def specialArray(nums: List[int]) -> int:
    N = len(nums) 
    # Count frequencies (like Counter), but have special place for N
    # We also ignore 0, since if X=0 then we return -1 anyways (0 numbers greater or equal to 0 is impossibe! if nums = [0] then we return -1 because count of 0 is 1)
    freq = [0] * (N + 1)
    for num in nums:
        freq[min(num, N)] += 1 # if num > N then this number is not special (there can't be more than N numbers in the array), so we put it in last place and ignore it
    # Counter number of elements that are >= than current element
    numGreaterThanOrEqualTo = 0
    # Iterate over N to 1 (0 is not included, because if there are 0 numbers, we should return -1)
    # Now we count prefixSum starting from the right of the freq array
    # Previous work done (count freq) is applied to current element, because if curr < prev then freq[curr] > freq[prev] by count
    # Here, i is acting like X
    for i in range(N, 0, -1):
        numGreaterThanOrEqualTo += freq[i]
        if numGreaterThanOrEqualTo == i: # If its equal to X
            return i
    return -1

if __name__ == "__main__":
    assert specialArray([3,5]) == 2
    assert specialArray([0,0]) == -1
    assert specialArray([0,4,3,0,4]) == 3