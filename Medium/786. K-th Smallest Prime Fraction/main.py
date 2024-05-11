"""
Runtime: 1558 ms beats 29%
Memory: 68.92 MB beats 48%
Time taken: 10 minutes 50 seconds
"""
import heapq
from typing import List
# Calculate arr[i] / arr[j], set smallest fraction = min(smallest_fraction, arr[i]/arr[j])
def kthSmallestPrimeFraction(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    min_heap = []

    # Calculate frac, add to min heap
    for i in range(n):
        for j in range(i+1, n):
            frac = arr[i] / arr[j]
            heapq.heappush(min_heap, (frac, arr[i], arr[j]))

    # Pop top-k minimum fracs
    for _ in range(k):
        last = heapq.heappop(min_heap)
    ans = [last[1], last[2]]
    return ans

if __name__ == "__main__":
    assert kthSmallestPrimeFraction(arr = [1,2,3,5], k = 3) == [2,5]
    assert kthSmallestPrimeFraction(arr = [1,7], k = 1) == [1,7]
