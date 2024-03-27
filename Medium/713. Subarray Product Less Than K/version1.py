"""
Option 1:
Start with first number, and use sliding window technique.
Then start with second number, and use sliding window technique.
Continue until we get to the last number.

Time complexity: O(n^2) because for each number we must iterate once over the array.

Example:
k = 100
nums = [10,5,2,6]

[10] : product=10, res=1
[10,5] : product=50, res=2
[10,5,2] : product=100, res=2

[5] : product=5, res=3
[5,2] : product=10, res=4
...
...

Got: Time Limit Exceeded, coding time: 11 minutes 30 seconds

"""
from typing import List
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    res = 0
    for starting_i in range(len(nums)):
        right = starting_i
        current_product = 1
        while right < len(nums):
            current_product *= nums[right]
            if current_product < k:
                res += 1
                right += 1
            else:
                break
    return res

if __name__ == "__main__":
    assert numSubarrayProductLessThanK([10,5,2,6], 100) == 8
    assert numSubarrayProductLessThanK([1,2,3], 0) == 0
    assert numSubarrayProductLessThanK([1,1,1], 1) == 0
    assert numSubarrayProductLessThanK([1,1,1], 2) == 6