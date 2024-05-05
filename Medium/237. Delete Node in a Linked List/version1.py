"""
Runtime: 44 ms beats 18%
Memory: 16.7 MB beats 70%
Time taken: 4 minutes 54 seconds
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    prev = node
    while node.next:
        node.val = node.next.val
        prev = node
        node = node.next
    prev.next = None

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