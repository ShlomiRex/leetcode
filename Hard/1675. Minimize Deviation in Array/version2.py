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

def increase_min_OR_decrease_max(nums: List[int], new_val: int, is_decrease_max: bool):
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

    print(f"Nums = {nums}, Deviation = {deviation}, Min = {min_elem}, Max = {max_elem}")


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        min_elem, max_elem = nums[0], nums[-1]

        # The goal: Minimize deviation.
        deviation = max_elem - min_elem

        while True:
            # Only if we couldn't increase max AND decrease min, then the program reached the goal of minimized deviation
            decreased_max = False
            increased_min = False

            # Decrease maximum
            if max_elem % 2 == 0:
                changed_max = int(max_elem / 2)

                abs_max = max(nums[-2], changed_max)
                abs_min = min(min_elem, changed_max)
                new_deviation = abs_max - abs_min

                if new_deviation < deviation:
                    decreased_max = True
                    increase_min_OR_decrease_max(nums, changed_max, is_decrease_max=True)
                    min_elem, max_elem = nums[0], nums[-1]
                    deviation = max_elem - min_elem
                    continue

            # Increase minimum
            if min_elem % 2 == 1:
                changed_min = int(min_elem) * 2

                abs_max = max(max_elem, changed_min)
                abs_min = min(nums[1], changed_min)
                new_deviation = abs_max - abs_min

                if new_deviation < deviation:
                    increased_min = True
                    increase_min_OR_decrease_max(nums, changed_min, is_decrease_max=False)
                    min_elem, max_elem = nums[0], nums[-1]
                    deviation = max_elem - min_elem
            # Check if we didn't change max AND min, which means, we are done.
            if not decreased_max and not increased_min:
                break

        return deviation