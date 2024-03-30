"""

Runtime: 266 ms beats 92%
Memory: 36 MB beats 38%
Time it took: 5 minutes, 25 seconds

First intuition: one pointer, walk in O(n) and store the numbers in order in array: [1,2,2,1]
Then iterate over array and check if palindrome.

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] != arr[r]:
            return False
        l, r = l+1, r-1
    return True

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    assert isPalindrome(head) == True

    head = ListNode(1, ListNode(2))
    assert isPalindrome(head) == False
