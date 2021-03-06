"""
Given a linked list, swap every two adjacent nodes and return its head.

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 
Constraints:

    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100
 
Follow up: Can you solve the problem without modifying the values in the list's nodes? (i.e., Only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        p = head
        while p:
            val = p.val

            if p.next:
                p.val = p.next.val
                p.next.val = val
                p = p.next

            p = p.next

        return head


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        def recur(head): 
            if not head or not head.next: 
                return head 


            p1 = head 
            p2 = head.next 
            
            p1.next = recur(p2.next)
            p2.next = p1 

            return p2 
        
        return recur(head)