# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    
    # Recursive call to process the rest of the list
    head.next = deleteDuplicates(head.next)
    
    # If current value is the same as the next value, skip the duplicate
    if head.val == head.next.val:
        head.next = head.next.next
    
    return head
            
if __name__ == "__main__":
    head = ListNode(1, ListNode(1, ListNode(2)))
    res = deleteDuplicates(head)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next == None

    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    res = deleteDuplicates(head)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next.val == 3
    assert res.next.next.next == None