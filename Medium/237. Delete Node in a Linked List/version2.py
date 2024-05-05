"""
Runtime: 37 ms beats 66%
Memory: 16.8 MB beats 13%

One liner solution, from solution section
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    node.val, node.next = node.next.val, node.next.next

if __name__ == "__main__":
    linkedlist = ListNode(4)
    linkedlist.next = ListNode(5)
    linkedlist.next.next = ListNode(1)
    linkedlist.next.next.next = ListNode(9)
    deleteNode(linkedlist.next)
    assert linkedlist.val == 4
    assert linkedlist.next.val == 1
    assert linkedlist.next.next.val == 9
    assert linkedlist.next.next.next == None

    linkedlist = ListNode(4)
    linkedlist.next = ListNode(5)
    linkedlist.next.next = ListNode(1)
    linkedlist.next.next.next = ListNode(9)
    deleteNode(linkedlist.next.next)
    assert linkedlist.val == 4
    assert linkedlist.next.val == 5
    assert linkedlist.next.next.val == 9
    assert linkedlist.next.next.next == None