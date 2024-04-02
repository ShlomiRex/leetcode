"""
Runtime: 28 ms beats 96%
Memory: 17.60 MB beats 97%
Time taken: 4 minutes 4 seconds

In this new version, I used 'next' pointer. In my previous answer I only used 'prev' and 'curr', which is more efficient. Somehow I got better runtime.
I completed this question on 02 April, 2024 (refresh my memory how to do this question).
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    curr = head
    next = curr.next
    prev = None
    while next:
        curr.next = prev
        prev = curr
        curr = next
        next = next.next
        curr.next = prev
    return curr

if __name__ == "__main__":
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
	newhead = reverseList(head)
	assert newhead.val == 5
	assert newhead.next.val == 4
	assert newhead.next.next.val == 3
	assert newhead.next.next.next.val == 2
	assert newhead.next.next.next.next.val == 1
 
 
	head = ListNode(1)
	newhead = reverseList(head)
	assert newhead.val == 1
 

	head = None
	newhead = reverseList(head)
	assert newhead == None
	
