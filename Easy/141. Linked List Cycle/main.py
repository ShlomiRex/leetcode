from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def hasCycle(head: Optional[ListNode]) -> bool:
	slow = head
	fast = head

	while slow != None and fast != None:
		slow = slow.next
		fast = fast.next
		if fast:
			fast = fast.next
		else:
			return False
		if slow == fast:
			return True

	return False

if __name__ == "__main__":
	a = ListNode(2, ListNode(0, ListNode(4)))
	a.next = a
	head = ListNode(3, a)
	assert hasCycle(head) == True
	
	a = ListNode(2)
	head = ListNode(1, a)
	a.next = head
	assert hasCycle(head) == True

	head = ListNode(1)
	assert hasCycle(head) == False

