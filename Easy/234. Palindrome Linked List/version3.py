"""

Runtime: 262 ms beats 95%
Memory: 32 MB beats 83%

Combine last code 2 lines into 1
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next # We access (fast.next).next so we need to check that fast.next exists, no None errors
    # We reached middle with slow pointer. Reverse

    prev = slow
    slow = slow.next
    prev.next = None
    
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    
    start_p, end_p = head, prev
    while end_p:
        if end_p.val != start_p.val:
            return False
        start_p, end_p = start_p.next, end_p.next
    return True

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    assert isPalindrome(head) == True

    head = ListNode(1, ListNode(2))
    assert isPalindrome(head) == False
