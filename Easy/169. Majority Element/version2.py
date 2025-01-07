"""
Boyer-Moore Voting Algorithm
O(n) time, O(1) space
"""
from collections import defaultdict
from typing import List

def majorityElement(nums: List[int]) -> int:
    curr_max = 0
    majority = nums[0]
    for n in nums:
        if n == majority:
            curr_max += 1
        else:
            # If we reached 0 we switch the majority element
            if curr_max == 0:
                majority = n
                curr_max = 1
            # We decrease the majority element count
            else:
                curr_max -= 1
    return majority

if __name__ == '__main__':
    assert majorityElement([3,2,3]) == 3
    assert majorityElement([2,2,1,1,1,2,2]) == 2
    assert majorityElement([2,2,2,2,2,1,1,1,1]) == 2
    assert majorityElement([1]) == 1
    
