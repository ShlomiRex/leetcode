"""

Runtime: 913 ms beats 35%
Memory: 30 MB beats 80%
Time it took: 1 hour

Reason it took 1 hour: I read incorrectkly; I thought the maximum is per subarray, not for the entire array.

First intuition: sliding window technique

nums = [1,3,2,3,3], k = 2

[1]           {1: 1}, max = 1
[1,3]         {1: 1, 3: 1}, max = 3
[1,3,2]       {1: 1, 3: 1, 2: 1}, max = 3 and freq > k
[1,3,2,3]     {1: 1, 3: 2, 2: 1} we got 3 appears at least k (2) times

NOTE: From this point we dont need to add more elements, since this rule will always hold true
increase res by the (len(nums) - right) = (5 - 3) = 2

res = 2

[3,2,3]      {1: 0, 3: 2, 2: 1} we increase res by (5 - 3) = 2  (because [3,2,3,3] also matches this rule), increase left
res = 4

[2, 3]       {1: 0, 3: 1, 2:1} maximum element (3) is not at least k. next

[2,3,3]      {1: 0, 3: 2, 2:1} we increase res by (5 - 4) = 1, increase left
res = 5

[3,3]        {1:0, 3: 2, 2:0} we increase res by (5 - 4) = 1, increase left
res = 6

[3]          {1:0, 3: 1, 2:0} increase right

right = len(nums) exit
return res=6

Cases:
nums[right] is new maximum in the subarray, we need to reset max_num



[3,1,2,2]  max=3
[1,2,2]    max=2, how do we know whats the new maximum after increasing left?


NOTE: The problem was I didn't read the question correctly.
The maximum element is NOT per subarray, its for the entire array!!!
"""
from typing import List

def countSubarrays(nums: List[int], k: int) -> int:
    num_good_subarrays = 0
    arr_max = max(nums)
    l, r = 0, 0
    freq = 0
    while r < len(nums):
        if nums[r] == arr_max:
            freq += 1
        while freq >= k:
            num_good_subarrays += (len(nums) - r)
            if nums[l] == arr_max:
                freq -= 1
            l += 1
        r += 1 # We incremenet here after finish processing (if not, we would reach update num_good_subarrays and wrong answer)
            
    return num_good_subarrays

"""
max = 3

[1,3,2,3,3]

[1] r+=1
[1,3] r+=1
[1,3,2] r+=1
[1,3,2,3] max_element > k, 
"""

if __name__ == "__main__":
    assert countSubarrays([1,3,2,3,3], 2) == 6
    assert countSubarrays([1,4,2,1], 3) == 0