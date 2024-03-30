"""

Runtime: 286 ms beats 62%
Memory: 31 MB beats 83%

After read solutions I need to use slow,fast pointers approach.
How does it work? the fast pointer will be at the end of the linked list and slow pointer will be at the middle,
but we can't go back and check in reverse, because its one-directional linked list.

So instead what we do is, when we reach middle (with slow pointer), the slow pointer will reverse the remaining half-linked list.
This allows us to start again from head, and start from the end of the linked list, and compare each element.

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
    
    start_p = head
    end_p = prev
    while end_p:
        if end_p.val != start_p.val:
            return False
        start_p = start_p.next
        end_p = end_p.next
    return True

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    assert isPalindrome(head) == True

    head = ListNode(1, ListNode(2))
    assert isPalindrome(head) == False
