from typing import List

"""

Runtime: beats 13%
Memory: beats 5%

"""

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    if len(nums) == 0 and k == 0: return True
    if len(nums) < 1: return False
    if len(nums) == 2: return nums[0] == nums[1] and k > 0

    my_map = {}
    for i,n in enumerate(nums):
        if n not in my_map: my_map[n] = {"count": 1,"index_list": [i]}
        else:
            my_map[n]["count"] += 1
            my_map[n]["index_list"].append(i)
    # print(my_map)
    for num in my_map:
        # If contains duplicate
        if my_map[num]["count"] >= 2:
            # Check range
            for i in range(len(my_map[num]["index_list"]) - 1):
                if abs(my_map[num]["index_list"][i] - my_map[num]["index_list"][i+1]) <= k:
                    return True
    return False


if __name__ == "__main__":
    assert containsNearbyDuplicate([1,2,3,1], 3) == True
    assert containsNearbyDuplicate([1,0,1,1], 1) == True
    assert containsNearbyDuplicate([1,2,3,1,2,3], 2) == False
    assert containsNearbyDuplicate([99, 99], 2) == True
    assert containsNearbyDuplicate([99], 1) == False
    assert containsNearbyDuplicate([99], 0) == False
    assert containsNearbyDuplicate([], 0) == True
    assert containsNearbyDuplicate([2,2], 3) == True
    assert containsNearbyDuplicate([-1, -1], 1) == True