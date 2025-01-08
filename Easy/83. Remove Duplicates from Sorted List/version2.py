# Definition for singly-linked list.
from typing import Optional

"""
Do not name a variable "nxt" is its not directly next of curr because it can be confusing.
My iterative answer.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    
    curr = head
    p = head.next

    while p:
        while p and curr.val == p.val:
            p = p.next

        curr.next = p
        curr = curr.next
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