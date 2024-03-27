"""
Note: this code doesn't work but its only meant to see what i have tried.

Option 2: some sort of memory? No, i need to use the left window

[10]: 10, res=1
[10, 5]: 50, res=2
[10, 5, 2]: 100, res=2

We increase left pointer, first element is new subarray: 
[10] so we increase res: res=3

[5, 2]: 10, res=4
[5, 2, 6]: 60, res=5

We increase left pointer, first element is new subarray:
[5] so we increase res: res=6

...


"""
from typing import List
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    res = 0
    
    left,right = 0,0
    current_product = 1
    while right < len(nums):
        current_product *= nums[right]
        if current_product < k:
            res += 1
            right += 1
        else:
            if nums[left] < k:
                res += 1
            current_product /= nums[left]
            left += 1
    return res

if __name__ == "__main__":
    assert numSubarrayProductLessThanK([10,5,2,6], 100) == 8
    assert numSubarrayProductLessThanK([1,2,3], 0) == 0
    assert numSubarrayProductLessThanK([1,1,1], 1) == 0
    assert numSubarrayProductLessThanK([1,1,1], 2) == 6
        