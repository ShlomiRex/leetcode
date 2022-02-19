from typing import List, Optional


def searchInsert(nums: List[int], target: int) -> int:
    """
    Binary search through sorted array nums the target.
    If target is not exist, return the insertion index.
    :param nums:
    :param target:
    :return:
    """
    start_i = 0
    end_i = len(nums) - 1
    while start_i <= end_i:
        mid = (end_i + start_i) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            end_i = mid - 1
        else:
            start_i = mid + 1
    return start_i


def increase_min(nums: List[int], new_min: int):
    return increase_min_OR_decrease_max(nums, new_min, is_decrease_max=False)


def decrease_max(nums: List[int], new_max: int):
    return increase_min_OR_decrease_max(nums, new_max, is_decrease_max=True)


def increase_min_OR_decrease_max(nums: List[int], new_val: int, is_decrease_max: bool) -> (int, int, int):
    """
    :param nums:
    :param new_max:
    :return:
    """
    if is_decrease_max:
        print(f"Decreased max from {nums[-1]} to {new_val}")
        # Pop the old max
        nums.pop(-1)
    else:
        print(f"Increased min from {nums[0]} to {new_val}")
        # Pop the old min
        nums.pop(0)

    # Insert the changed element to the sorted array
    insertion_index = searchInsert(nums, new_val)
    nums.insert(insertion_index, new_val)

    # Return deviation
    min_elem = nums[0]
    max_elem = nums[-1]
    deviation = max_elem - min_elem

    print(f"Nums = {nums}, Deviation = {deviation}")

    return min_elem, max_elem, deviation


def minimumDeviation(nums: List[int]) -> int:
    # We don't care about duplicate numbers. In fact, less numbers = more efficient searches and inserts.
    nums = list(set(nums))
    # We don't care about indexes, so we can sort. This helps with finding minimum, maximum.
    nums = sorted(nums)
    print(nums)

    min_elem = nums[0]
    max_elem = nums[-1]

    # The goal: Minimize deviation.
    deviation = max_elem - min_elem
    print(f"Deviation: {deviation}")

    while True:
        # Only if we couldn't increase max AND decrease min, then the program reached the goal of minimized deviation
        decreased_max = False
        increased_min = False

        # Decrease maximum
        if max_elem % 2 == 0:
            changed_max = int(max_elem / 2)
            # If we divide, we can't set the max if it's less than the minimum. We can't have deviation of negative!
            if changed_max > min_elem:
                # Check that this operation decreased deviation
                new_deviation = changed_max - min_elem
                if new_deviation < deviation:
                    decreased_max = True
                    min_elem, max_elem, deviation = decrease_max(nums, changed_max)

        # Increase minimum
        if min_elem % 2 == 1:
            changed_min = int(min_elem) * 2
            # If we multiply, we can't set the min if it's more than the maximum. We can't have deviation of negative!
            if changed_min < max_elem:
                # Check that this operation decreased deviation
                new_deviation = max_elem - changed_min
                if new_deviation < deviation:
                    increased_min = True
                    min_elem, max_elem, deviation = increase_min(nums, changed_min)
        # Check if we didn't change max AND min, which means, we are done.
        if not decreased_max and not increased_min:
            break

    return deviation


if __name__ == "__main__":
    # nums = [4, 4, 1, 2, 2, 2, 3, 4, 4, 4]
    # res = minimumDeviation(nums)
    # print(res)
    # assert res == 1
    #
    # nums = [1, 2, 3, 4]
    # res = minimumDeviation(nums)
    # print(res)
    # assert res == 1
    #
    # nums = [4, 1, 5, 20, 3]
    # res = minimumDeviation(nums)
    # print(res)
    # assert res == 3
    #
    # nums = [2, 10, 8]
    # res = minimumDeviation(nums)
    # print(res)
    # assert res == 3

    nums = [3, 5]
    res = minimumDeviation(nums)
    print(res)
    assert res == 1
    #
    # nums = [5, 8]
    # res = minimumDeviation(nums)
    # print(res)
    # assert res == 1
