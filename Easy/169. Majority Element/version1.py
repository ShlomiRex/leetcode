"""
Use hashmap to store the frequency of each element in the list.
O(n) time, O(n) space
"""
from collections import defaultdict
from typing import List

def majorityElement(nums: List[int]) -> int:
    hashmap = defaultdict(int)
    curr_max = 0
    majority = None
    for n in nums:
        hashmap[n] += 1
        if hashmap[n] > curr_max:
            curr_max = hashmap[n]
            majority = n
    return majority

if __name__ == '__main__':
    assert majorityElement([3,2,3]) == 3
    assert majorityElement([2,2,1,1,1,2,2]) == 2
    assert majorityElement([2,2,2,2,2,1,1,1,1]) == 2
    assert majorityElement([1]) == 1
    
