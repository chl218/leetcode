"""
Given the head of a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two
partitions.


Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [1,4,3,0,5,2], x = 2
Output: [1,0,4,3,5,2]


Constraints:

    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200

"""


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        toFront = []

        p = head
        while p:
            if p.val < x:
                toFront.append(p.val)
            p = p.next

        p = head
        while p and toFront:
            val = toFront.pop(0)

            if p.val >= x:
                toFront.append(p.val)

            p.val = val
            p = p.next

        return head
