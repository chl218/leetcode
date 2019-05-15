/**

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

**/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    
    if(head == NULL) {
        return false;
    }
    
    struct ListNode *p = head, *q = head;
    
    while(q != NULL && q->next != NULL) {
        p = p->next;
        q = q->next->next;
        if(p == q) {
            return true;
        }
    }
    return false;
}