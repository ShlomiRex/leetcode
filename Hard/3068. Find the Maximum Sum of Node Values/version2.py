"""
Runtime: 937 ms beats 93%
Memory: 28.22 MB beats 38%

Cleaned-up solution
"""
from typing import List
def maximumValueSum(nums: List[int], k: int, edges: List[List[int]]) -> int:
    n = len(nums)
    currMaxSum = sum(nums)
    
    benefit = [0] * n
    for i in range(n):
        benefit[i] = (nums[i] ^ k) - nums[i]
    
    benefit.sort(reverse=True)

    for i in range(0, n-1, 2):
        benSum = benefit[i] + benefit[i+1]
        if benSum > 0:
            currMaxSum += benSum
        else:
            break
    
    return currMaxSum

if __name__ == "__main__":
    assert maximumValueSum(nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]) == 6
    assert maximumValueSum(nums = [2,3], k = 7, edges = [[0,1]]) == 9
    assert maximumValueSum(nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]) == 42
    assert maximumValueSum(nums = [2,3,2], k = 7, edges = [[0,1],[1,2]]) == 13
    assert maximumValueSum(nums = [2,3,2,4], k = 7, edges = [[0,1],[1,2],[2,3]]) == 17
