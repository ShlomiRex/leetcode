from typing import List

"""
Runtime: 34ms beats 93%
Memory: 16MB beats 67%

We go back backwards so that we don't overwrite out nums1 array.
This is the best solution O(m+n) time.
Its like we have 3 pointers:
    i - pointer to where the next non-descending number will go (in nums1)
    p1 - pointer to the number in nums1 to be compared against
    p2 - pointer to the number in nums2 to be compared against
"""

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1, p2 = m-1, n-1

    for i in range(m+n - 1, -1, -1):
        if p2 == -1:
            break

        if p1 == -1:
            nums1[i] = nums2[p2]
            p2 -= 1
            continue

        if nums2[p2] >= nums1[p1]:
            nums1[i] = nums2[p2]
            p2 -= 1
        else:
            nums1[i] = nums1[p1]
            p1 -= 1

    #     print(f"i: {i}, num1: {num1}, num2: {num2}, p1: {p1}, p2: {p2}, nums1: {nums1}")
    # print(nums1)

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    assert nums1  == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    merge(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [0]
    merge(nums1, 0, [1], 1)
    assert nums1 == [1]

    nums1 = [2,0]
    merge(nums1, 1, [1], 1)
    assert nums1 == [1, 2]