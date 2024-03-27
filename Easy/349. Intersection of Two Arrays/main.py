"""

Runtime: 40ms beats 91%
Memory: 16MB beats 90%
Time it took to solve: 5 minutes, 50 seconds

Option 1: Sort arrays, convert them to set, iterate over them both, and store the visited numbers in a hashmap or set to know in O(1) if we visited that number before. If yes its intersection. Time complexity: Sort: O(n log n), Convert to set: O(n), Iterate: O(n).

Option 2: Only use hashmap/set to store visited numbers. Iterate over the first array, add to set. Iterate over second array and check if current number is visited. Time complexity: O(n+m), Auxulary memory: O(n+m)

I chose option 2, since its more simple and also we don't need to sort.
"""

from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    visited = set()
    intersection = set()
    for i in range(len(nums1)):
        visited.add(nums1[i])
    for j in range(len(nums2)):
        if nums2[j] in visited:
            intersection.add(nums2[j])
    return intersection

if __name__ == '__main__':
    assert list(intersection([1,2,2,1], [2,2])) == [2]
    assert list(intersection([4,9,5], [9,4,9,8,4])) == [9,4]