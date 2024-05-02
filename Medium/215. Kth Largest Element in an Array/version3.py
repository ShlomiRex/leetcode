"""
Runtime: 473 ms beats 58%
Memory: 29.96 MB beats 35%
"""
from typing import List
import heapq
def findKthLargest(nums: List[int], k: int) -> int:
    heap = [-num for num in nums]
    heapq.heapify(heap)
    for _ in range(k):
        ans = heapq.heappop(heap)
    return -ans

if __name__ == "__main__":
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4