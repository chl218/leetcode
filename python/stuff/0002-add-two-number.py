"""You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.



Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

    The number of nodes in each linked list is in the range [1, 100].

    0 <= Node.val <= 9

    It is guaranteed that the list represents a number that does not have
    leading zeros.

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        p = l1
        q = l2
        p_tail = None
        q_tail = None
        while p and q:
            p_tail, q_tail =  p, q
            p, q = p.next, q.next

        if p and not q:
            while p:
                q_tail.next = ListNode(0, None)
                q_tail = q_tail.next
                p = p.next
        elif q and not p:
            while q:
                p_tail.next = ListNode(0, None)
                p_tail = p_tail.next
                q = q.next


        carry = 0
        h = ListNode()
        p = h
        q = h
        while l1 and l2:
            if carry + l1.val + l2.val > 9:
                p.val = (carry + l1.val + l2.val) % 10
                carry = (carry + l1.val + l2.val) // 10
            else:
                p.val = carry + l1.val + l2.val
                carry = 0

            l1 = l1.next
            l2 = l2.next

            q = p
            p.next = ListNode()
            p = p.next


        if carry != 0:
            p.val = carry
            return h
        else:
            q.next = None
            return h