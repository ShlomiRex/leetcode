from typing import List

"""
time limit reached
"""

def canPartition(nums: List[int]) -> bool:
    if nums is None or len(nums) < 2:
        return False
    totalSum = sum(nums)
    if totalSum % 2 != 0:
        return False

    target = totalSum / 2

    success = False
    subsums = []
    def dfs(candidates: List[int], target: int, cur: List[int]):
        nonlocal success
        if success:
            return
        if target == 0:
            success = True
            subsums.append(cur)
            return
        if target < 0:
            return
        for candidate in candidates:
            new_candidates = candidates.copy()
            new_candidates.remove(candidate)
            dfs(new_candidates, target - candidate, cur + [candidate])

    dfs(nums, target, [])
    if success:
        print("Possible partition: ", subsums)
    return success

if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print("nums", nums)
    res = canPartition(nums)
    assert res == True

    nums = [1,2,3,5]
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
