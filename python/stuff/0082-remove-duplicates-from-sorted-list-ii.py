"""
Given the head of a sorted linked list, delete all nodes that have duplicate
numbers, leaving only distinct numbers from the original list. Return the
linked list sorted as well.


Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]


Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cmap = {}

        p = head
        while p:
            if p.val not in cmap:
                cmap[p.val] = True
            else:
                cmap[p.val] = False
            p = p.next

        p, q = head, head
        while p:
            if cmap[p.val]:
                q, p = p, p.next
            else:

                while p and not cmap[p.val]:
                    p = p.next

                if not cmap[q.val]:
                    head = p
                else:
                    q.next = p

        return head



# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#     sentinel = ListNode(0, head)
#     pred = sentinel
#
#     while head:
#         if head.next and head.val == head.next.val:
#             while head.next and head.val == head.next.val:
#                 head = head.next
#             pred.next = head.next
#         else:
#             pred = pred.next
#         head=head.next
#
#     return sentinel.next