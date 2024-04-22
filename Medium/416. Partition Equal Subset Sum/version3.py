"""
Runtime: 156 ms beats 98%
Memory: 17.76 MB beats 75%

Intuition: think about each element. Do we add it to the subarray or not? If yes, our current sum is the element. If not, we stay with current sum of 0.
We keep track of all the sums we have. If its target, we return True.
We keep adding all possible sums with current element.
"""
from typing import List
def canPartition(nums: List[int]) -> bool:
    totalSum = sum(nums)
    # If not even
    if totalSum % 2 != 0:
        return False
    if len(nums) == 0:
        return True
    target = totalSum // 2
    allPossibleSums = set()
    allPossibleSums.add(0)

    for i in range(len(nums)):
        sums_to_add = []
        for _sum in allPossibleSums:
            sums_to_add.append(_sum + nums[i])
        allPossibleSums.update(sums_to_add)
        if target in allPossibleSums:
            return True
    return False

if __name__ == "__main__":
    assert canPartition([1, 5, 11, 5]) == True
    assert canPartition([1, 2, 3, 5]) == False
    assert canPartition([1, 2, 3]) == True
    assert canPartition([1]) == False
    assert canPartition([0, 1, 0, 1, 0, 1, 0, 1]) == True
    assert canPartition([0, 1, 0, 1, 0, 1, 0, 1, 0]) == True
    assert canPartition([0, 1, 0, 1, 0, 1, 0, 1, 0, 4]) == True
    assert canPartition([0, 1, 0, 1, 0, 1, 0, 1, 0, 3]) == False
    assert canPartition([2, 1, 5]) == False
    assert canPartition([1, 2, 5]) == False
