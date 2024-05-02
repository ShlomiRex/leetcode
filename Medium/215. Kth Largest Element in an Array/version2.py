"""
Runtime: 494 ms beats 30%
Memory: 29.6 MB beats 78%
Time taken: 4 minutes 47 seconds
"""
from typing import List
import heapq
def findKthLargest(nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
    for _ in range(k):
        ans = heapq.heappop(heap)
    return -ans

if __name__ == "__main__":
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4