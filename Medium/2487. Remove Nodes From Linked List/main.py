"""
Runtime: 491 ms beats 26%
Memory: 51.1 MB beats 78%
Time taken: 31 minutes, 10 seconds

I mostly had issues with the deleting node and updating next/prev. I got confused there.
"""
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    # Convert linked list to list
    # Start from right to left: calculate maximum value to the right
    # Delete every node with rightPrefix[i] > curr_node.val

    lst = []
    curr = head
    while curr:
        lst.append(curr.val)
        curr = curr.next
    n = len(lst)
    rightPrefix = [0] * n
    curr_right_max = 0
    for i in range(n-2, -1, -1):
        curr_right_max = max(curr_right_max, lst[i+1])
        rightPrefix[i] = curr_right_max
    
    
    dummy = ListNode(0, head)
    prev = dummy
    curr = dummy.next
    i = 0
    while curr:
        if curr.val < rightPrefix[i]:
            # Delete this node
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
        i += 1
    curr = dummy.next
    while curr:
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
    res = removeNodes(head)
    assert res.val == 13
    assert res.next.val == 8
    assert res.next.next == None