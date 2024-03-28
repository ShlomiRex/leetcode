from typing import List

"""

Sliding window of size K technique
Runtime: beats 5%
Memory: beats 98%

"""

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    sliding_window_nums = []
    for n in nums:
        if n in sliding_window_nums: 
            return True
        else:
            sliding_window_nums.append(n)
            if len(sliding_window_nums) > k:
                sliding_window_nums.pop(0)
    return False


if __name__ == "__main__":
    assert containsNearbyDuplicate([1,2,3,1], 3) == True
    assert containsNearbyDuplicate([1,0,1,1], 1) == True
    assert containsNearbyDuplicate([1,2,3,1,2,3], 2) == False
    assert containsNearbyDuplicate([99, 99], 2) == True
    assert containsNearbyDuplicate([99], 1) == False
    assert containsNearbyDuplicate([99], 0) == False
#    assert containsNearbyDuplicate([], 0) == True
    assert containsNearbyDuplicate([2,2], 3) == True
    assert containsNearbyDuplicate([-1, -1], 1) == True