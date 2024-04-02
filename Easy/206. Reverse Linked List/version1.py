"""
Runtime: 39 ms, faster than 79.43% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 76.36% of Python3 online submissions for Reverse Linked List.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
	prev, cur = None, head
	while cur:
		tmpnxt = cur.next
		cur.next = prev
		prev = cur
		cur = tmpnxt
	return prev

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
	
