"""
Runtime: 433 ms beats 93%
Memory: 300 MB beats 36%
Time taken: 1 minute
Idiot solution but it works and surprisingly it beats 93% in runtime.
"""
from typing import List
def findKthLargest(nums: List[int], k: int) -> int:
    return sorted(nums)[len(nums)-k]

if __name__ == "__main__":
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4