
class ListNode:
    """ Definition for singly-linked list
    """
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(node: ListNode):
    """ Delete Node in a Linked List
    Write a function to delete a node (except the tail) in a singly linked list,
    given only access to that node.

    Note:
        - The linked list will have at least two elements.
        - All of the nodes' values will be unique.
        - The given node will not be the tail and it will always be a valid node
            of the linked list.
        - Do not return anything from your function.
    """

    old_node = node.next

    node.next = old_node.next
    node.val = old_node.val

    old_node.Next = None


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """Remove Nth Node From End of List

    Given a linked list, remove the n-th node from the end of list and return
    its head.

    Example:
    Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end, the linked list becomes
    1->2->3->5.

    Note: Given n will always be valid.
    Follow up: Could you do this in one pass?
    """

    t = None
    p = head
    q = head
    for i in range(n-1):
        q = q.next

    while q.next is not None:
        t = p
        p = p.next
        q = q.next

    if t is None:
        head = head.next
    else:
        t.next = p.next

    return head


def reverseList(head: ListNode) -> ListNode:
    """Reverse Linked List

    Reverse a singly linked list.
    """
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev
