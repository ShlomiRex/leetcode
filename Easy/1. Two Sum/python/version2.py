from typing import List

"""
Runtime: 82 ms, faster than 67.83% of Python3 online submissions for Two Sum.
Memory Usage: 15.2 MB, less than 58.91% of Python3 online submissions for Two Sum.
"""

def twoSum(nums: List[int], target: int) -> List[int]:
    hashtable = {}
    ans = []

    # Find ans O(n)
    for i, n in enumerate(nums):
        if n not in hashtable:
            hashtable[n] = i
        if (target - n) in hashtable:
            second_index = hashtable[target-n]
            if second_index != i:
                ans = [i, second_index]
                break
    return ans


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    res = twoSum(nums, target)
    print(res)
    assert res == [0, 1]

    nums = [3, 2, 4]
    target = 6
    res = twoSum(nums, target)
    print(res)
    assert res == [1, 2]

    nums = [3, 3]
    target = 6
    res = twoSum(nums, target)
    print(res)
    assert res == [0, 1]

    nums = [2, 3, 3]
    target = 6
    res = twoSum(nums, target)
    print(res)
    assert res == [1, 2]

    nums = [0, 0, 0, 0, 1, 1, 6, 0, 0]
    target = 6
    res = twoSum(nums, target)
    print(res)
    assert res == [0, 6]

    nums = [0, 0, 0, 0, 1, 1, 6, 0, 0]
    target = 6
    res = twoSum(nums, target)
    print(res)
    assert res == [0, 6]

    nums = [6, -3]
    target = 3
    res = twoSum(nums, target)
    print(res)
    assert res == [0, 1]