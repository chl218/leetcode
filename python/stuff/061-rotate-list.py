"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]


Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 10^9

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        n = 0
        p = head
        while p:
            p = p.next
            n += 1

        while k >= n:
            k %= n

        tail = n - k - 1

        p = head
        for i in range(tail):
            p = p.next

        q = p.next
        p.next = None

        stack = []
        while q:
            stack.append(q)
            t = q.next
            q.next = None
            q = t

        while stack:
            h = stack.pop()
            h.next = head
            head = h

        return head