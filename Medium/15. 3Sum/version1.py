"""
Almost correct answer. This solution contains duplicates, however.
"""
from collections import defaultdict
from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    #nums.sort() # O(n log n)

    hashmap = defaultdict(List[int])
    for i, num in enumerate(nums):
        if num not in hashmap:
            hashmap[num] = []
        hashmap[num].append(i)
    # Second pass, two sum
    ans = []
    for i, target in enumerate(nums):
        for j, a in enumerate(nums, i):
            b = -target - a
            if i != j and b in hashmap:
                indxs = hashmap[b]
                for ind in indxs:
                    if ind != i and ind != j:
                        #print(f"Adding: {[target, a, b]}, indexes: {[i, j, ind]}")
                        ans.append([target, a, b])
                        break
    return ans

if __name__ == "__main__":
    res = threeSum([-1,0,1,2,-1,-4])
    correct_answers = [[-1,-1,2],[-1,0,1]]
    for ans in correct_answers:
        assert ans in res


    res = threeSum([0,1,1])
    assert res == []

    res = threeSum([0,0,0])
    print(res)
    assert res == [[0,0,0]]