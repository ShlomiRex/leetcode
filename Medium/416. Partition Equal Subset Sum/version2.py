import math
from typing import List

"""
Runtime: 482 ms, faster than 80.55% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 14.6 MB, less than 71.63% of Python3 online submissions for Partition Equal Subset Sum.
"""

"""
Huge credit to:
https://www.youtube.com/watch?v=IsvocB5BJhw&t=244s
The algorithm is not mine, but I implimented the algo without looking at the code.

Time complexity analysis:
The size of the set 'allPossibleSums' is limited to the value of target.

First loop: O(n)
Check if target in allPossibleSums: O(1) average, in worst case: O(N)
So far: O(N^2)

Convert set to list: O(N)
Check if sum in the stack: O(N) worst case, O(1) average

Total: O(N^2 + N + N + N) = O(N^2)

The video says: O(sum(nums)) which in some cases can be worst than N^2
"""


def canPartition(nums: List[int]) -> bool:
    if nums is None or len(nums) < 2:
        return False
    totalSum = sum(nums)
    if totalSum % 2 != 0:
        return False

    target = totalSum / 2

    allPossibleSums = set()
    allPossibleSums.add(0)

    for i in range(len(nums) - 1, -1, -1):
        if target in allPossibleSums:
            return True
        num = nums[i]
        stack = list(allPossibleSums)
        for _sum in stack:
            # Option 1: Take num to the sum
            allPossibleSums.add(_sum + num)
            # Option 2: Don't take num to the sum
            allPossibleSums.add(_sum)
    return False


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print("nums", nums)
    res = canPartition(nums)
    assert res == True

    nums = [1, 2, 3, 5]
    print("nums", nums)
    res = canPartition(nums)
    assert res == False

    nums = [1, 2, 3]
    print("nums", nums)
    res = canPartition(nums)
    assert res == True

    nums = [1]
    print("nums", nums)
    res = canPartition(nums)
    assert res == False

    nums = None
    print("nums", nums)
    res = canPartition(nums)
    assert res == False

    nums = [0, 1, 0, 1, 0, 1, 0, 1]
    print("nums", nums)
    res = canPartition(nums)
    assert res == True

    nums = [0, 1, 0, 1, 0, 1, 0, 1, 0]
    print("nums", nums)
    res = canPartition(nums)
    assert res == True

    nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 4]
    print("nums", nums)
    res = canPartition(nums)
    assert res == True

    nums = [0, 1, 0, 1, 0, 1, 0, 1, 0, 3]
    print("nums", nums)
    res = canPartition(nums)
    assert res == False

    nums = [2, 1, 5]
    print("nums", nums)
    res = canPartition(nums)
    assert res == False

    nums = [1, 2, 5]
    print("nums", nums)
    res = canPartition(nums)
    assert res == False
