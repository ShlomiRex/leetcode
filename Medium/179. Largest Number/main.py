"""
Runtime: 26 ms beats 99%
Memory: 16.5 MB beats 28%
"""

from typing import List
import functools

def largestNumber(nums: List[int]) -> str:
    def custom_sort(a, b):
        if str(a)+str(b) > str(b)+str(a): return 1
        elif str(a)+str(b) < str(b)+str(a): return -1
        else: return 0
    nums.sort(key=functools.cmp_to_key(custom_sort), reverse=True)
    ans = ''.join(map(str, nums))
    if ans[0] == '0':
        return "0"
    return ans

if __name__ == "__main__":
    assert largestNumber([10, 2]) == "210"
    assert largestNumber([3,30,34,5,9]) == "9534330"
    assert largestNumber([0, 0]) == "0"