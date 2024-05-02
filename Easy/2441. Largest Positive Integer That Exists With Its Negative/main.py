"""
Runtime: 110 ms beats 54%
Memory: 16.8 MB beats 23%
Time taken: 2 minutes 58 second
"""
from typing import List
def findMaxK(nums: List[int]) -> int:
    hashset = set()
    ans = -1
    for num in nums:
        if (-num) in hashset:
            ans = max(ans, num, -num)
        hashset.add(num)
    return ans
            
if __name__ == "__main__":
    assert findMaxK([-1,2,-3,3]) == 3
    assert findMaxK([-1,10,6,7,-7,1]) == 7
    assert findMaxK([-10,8,6,7,-2,-3]) == -1