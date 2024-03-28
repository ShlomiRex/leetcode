"""

Time taken: 32m 37s
Runtime: 1154ms beats 58%
Memory: 31MB beats 74%

nums = [1,2,1,2,1,2,1,2], k = 1

left,right = 0,0

[1], freq={1: 1}, left=0, right=1
[1,2], freq={1:1, 2:1}, left=0, right=2
[1,2,1], freq={1:1}

First intuition:
I would use hashmap to count frequency of each element
Then I would use sliding window technique to check each subarray
I increase right pointer each time until the nums[right] element appears more than k
If it appears more than k, I start moving left pointer, until we have 'good' array, and update the hashmap

After I failed to implement the above, I read the solutions page with intuition how to implement:
1. Initialize l,r pointers
2. Initialize hashmap to store frequencies
3. Iterate through the array from left to right using the right pointer
4. Increment frequency of nums[r]
5. If the frequency of nums[r] exceeds k, we need to shrink the window from left until the frequency of nums[r] decrease by one.
6. Update maximum length of good subarray
7. Return result

"""
from typing import List
def maxSubarrayLength(nums: List[int], k: int) -> int:
    good_length, l, r = 0, 0, 0
    freq = {}
    while r < len(nums):
        if nums[r] not in freq:
            freq[nums[r]] = 1
        else:
            freq[nums[r]] += 1
        
        # Remember: good frequency is less than or equal to K, so here we check >k which means bad array
        # So we need here to shrink left window
        while freq[nums[r]] > k:
            freq[nums[l]] -= 1
            l += 1
        good_length = max(good_length, r - l + 1)
        r += 1
    return good_length

if __name__ == "__main__":
    assert maxSubarrayLength([1,2,3,1,2,3,1,2], 2) == 6
    assert maxSubarrayLength([1,2,1,2,1,2,1,2], 1) == 2
    assert maxSubarrayLength([5,5,5,5,5,5,5], 4) == 4
