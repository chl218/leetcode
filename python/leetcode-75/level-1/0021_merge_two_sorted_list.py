"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


Example 2:
Input: list1 = [], list2 = []
Output: []


Example 3:
Input: list1 = [], list2 = [0]
Output: [0]



Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        head = None
        tail = None
        while list1 and list2:

            if list1.val == list2.val:

                t1 = list1
                t2 = list2

                list1 = list1.next
                list2 = list2.next

                t1.next = t2
                t2.next = None

                if not head:
                    head = t1
                    tail = t2
                else:
                    tail.next = t1
                    tail = t2

            elif list1.val < list2.val:

                t1 = list1
                list1 = list1.next

                t1.next = None

                if not tail:
                    head = t1
                    tail = t1
                else:
                    tail.next = t1
                    tail = t1

            elif list1.val > list2.val:

                t2 = list2
                list2 = list2.next

                t2.next = None

                if not tail:
                    head = t2
                    tail = t2
                else:
                    tail.next = t2
                    tail = t2


        if list1:
            if not head:
                head = list1
            else:
                tail.next = list1

        if list2:
            if not head:
                head = list2
            else:
                tail.next = list2

        return head

