from typing import List

"""
Runtime: 140 ms, faster than 73.80% of Python3 online submissions for Single Number.
Memory Usage: 16.9 MB, less than 6.22% of Python3 online submissions for Single Number.
"""

def singleNumber(nums: List[int]) -> int:
    table = {}

    for num in nums:
        if num in table:
            if table[num] == 1:
                table.pop(num)
        else:
            table[num] = 1

    return list(table.keys())[0]


if __name__ == "__main__":
    nums = [2,2,1]
    res = singleNumber(nums)
    print(res)
    assert res == 1

    nums = [4,1,2,1,2]
    res = singleNumber(nums)
    print(res)
    assert res == 4

    nums = [1, 2, 2]
    res = singleNumber(nums)
    print(res)
    assert res == 1