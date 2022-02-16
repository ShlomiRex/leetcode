# Definition for singly-linked list.
from typing import Optional

"""
Runtime: 36 ms, faster than 62.34% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.8 MB, less than 90.54% of Python3 online submissions for Swap Nodes in Pairs.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    tail = head

    while tail is not None:
        next_tail = tail.next
        if next_tail is None:
            break
        tmp_tail_val = tail.val
        tail.val = next_tail.val
        next_tail.val = tmp_tail_val

        tail = tail.next.next

    return head


if __name__ == "__main__":
    lst = None
    res = swapPairs(lst)
    assert res is None

    lst = ListNode(1)
    res = swapPairs(lst)
    assert res.val == 1 and res.next is None

    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    res = swapPairs(lst)
    assert res.val == 2 and res.next.val == 1 and res.next.next.val == 4 and res.next.next.next.val == 3 and res.next.next.next.next is None

    lst = ListNode(1, ListNode(2, ListNode(3)))
    res = swapPairs(lst)
    assert res.val == 2 and res.next.val == 1 and res.next.next.val == 3 and res.next.next.next is None
