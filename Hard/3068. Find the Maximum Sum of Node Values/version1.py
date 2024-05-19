"""
Runtime: 1033 ms beats 30.11%
Memory: 28.53 MB beats 19.8%
Time taken: 1 hour 44 minutes

I needed to get hints. I did not look at code solution, only hints. But then I got stuck, and only the i+=2 was at the end (it was i+=1 small bug fix)

==================================================================

Understand what we maximize: 
choose edge (u,v), nums[u] = nums[u] XOR k, nums[v] = nums[v] XOR k,
maximize sum(nums[u] XOR k + nums[v] XOR k)

0 xor 0 = 0
0 xor 1 = 1
1 xor 0 = 1
1 xor 1 = 0

So we want to choose

"""
from typing import List
def maximumValueSum(nums: List[int], k: int, edges: List[List[int]]) -> int:
    n = len(nums)
    currMaxSum = sum(nums)
    xored = [0] * n
    for i, num in enumerate(nums):
        xored[i] = (num ^ k)
    
    benefit = [0] * n
    for i in range(n):
        benefit[i] = (xored[i] - nums[i], i)
    
    benefit.sort(reverse=True)
    #print(benefit)

    testSum = 0
    i = 0
    while i+1 < n:
        a = benefit[i]
        b = benefit[i+1]
        benSum = a[0] + b[0]
        if benSum > 0:
            currMaxSum += benSum
        else:
            break
        i += 2
    

    # maxed = [0] * n
    # for i in range(n):
    #     maxed[i] = max(nums[i], xored[i])
    # print(maxed)

    # maxed = [0] * n
    # for i in range(n):
    #     maxed[i] = max(xored[i], nums[i])
    # currMaxSum = max(currMaxSum, sum(maxed))
    return currMaxSum

if __name__ == "__main__":
    assert maximumValueSum(nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]) == 6
    assert maximumValueSum(nums = [2,3], k = 7, edges = [[0,1]]) == 9
    assert maximumValueSum(nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]) == 42
