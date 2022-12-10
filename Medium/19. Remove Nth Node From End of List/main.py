# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List

def removeNthFromEnd(head: ListNode, n: int) -> Optional[ListNode]:
	if head == None:
		return None
	
	nth_node_prev = None

	cur = head
	index = 0
	while cur != None:
		index += 1

		if index > n:
			if nth_node_prev == None:
				nth_node_prev = head
			else:
				nth_node_prev = nth_node_prev.next

		cur = cur.next
		
	if nth_node_prev:
		nth_node_prev.next = nth_node_prev.next.next
	else:
		if index == n:
			# extreme case, remove first link
			head = head.next
			return head
		else:
			return None

	return head


if __name__ == "__main__":
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
	res = removeNthFromEnd(head, 2)
	assert res.val == 1
	assert res.next.val == 2
	assert res.next.next.val == 3
	assert res.next.next.next.val == 5

	head = ListNode(1, None)
	res = removeNthFromEnd(head, 1)
	assert res == None

	head = ListNode(1, ListNode(2, None))
	res = removeNthFromEnd(head, 1)
	assert res.val == 1
	assert res.next == None

	head = ListNode(1, ListNode(2, None))
	res = removeNthFromEnd(head, 2)
	assert res.val == 2
	assert res.next == None

	head = ListNode(1, ListNode(2, ListNode(3, None)))
	res = removeNthFromEnd(head, 3)
	assert res.val == 2
	assert res.next.val == 3
	assert res.next.next == None