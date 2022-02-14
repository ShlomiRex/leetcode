# Definition for singly-linked list.
from typing import Optional

"""
Runtime: 32 ms, faster than 96.35% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.1 MB, less than 69.84% of Python3 online submissions for Merge Two Sorted Lists.
"""

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	def __str__(self) -> str:
		return f'{self.val} -> {self.next}'


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
	if list1 == None:
		return list2
	if list2 == None:
		return list1
	
	res = ListNode()
	if list1.val <= list2.val:
		res.next = ListNode(list1.val)
		list1 = list1.next
	else:
		res.next = ListNode(list2.val)
		list2 = list2.next
 
	while list1 != None and list2 != None:
		if list1.val <= list2.val:
			res.next = ListNode(list1.val)
			list1 = list1.next
		else:
			res.next = ListNode(list2.val)
			list2 = list2.next

	return res


if __name__ == "__main__":
	lst1 = ListNode(1, ListNode(2, ListNode(4)))
	lst2 = ListNode(1, ListNode(3, ListNode(4)))
	print("List 1:", lst1)
	print("List 2:", lst2)
	res = mergeTwoLists(lst1, lst2)
	print(res)
