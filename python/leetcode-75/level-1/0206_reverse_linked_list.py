"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the
reversed list.


Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


Example 2:
Input: head = [1,2]
Output: [2,1]


Example 3:
Input: head = []
Output: []


Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000



Follow up: A linked list can be reversed either iteratively or recursively.
Could you implement both?

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []

        while head:
            stack.append(head)
            head = head.next

        head = None
        tail = None
        if stack:
            head = stack.pop()
            head.next = None
            tail = head

        while stack:
            tail.next = stack.pop()
            tail = tail.next
            tail.next = None

        return head



# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev = None
#         while head:
#             curr = head
#             head = head.next
#             curr.next = prev
#             prev = curr
#         return prev