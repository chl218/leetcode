/**
Given a linked list, remove the n-th node from the end of list and return its
head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

**/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {

    if(n == 1 && head->next == NULL){
        free(head);
        return NULL;
    }   
    
    
    struct ListNode *p = head, *q = head;
    
    for(int i = 0; i < n; i++) {
        q = q->next;
    }
    
    if(q == NULL) {
        head = head->next;
        free(p);
        return head;
    }
    
    while(q->next != NULL) {
        p = p->next;
        q = q->next;
    }
    
    if(p->next == q) {
        p->next = NULL;
        free(q);
        return head;
    }
    
    struct ListNode *rm = p->next;
    p->next = p->next->next;
    free(rm);
    return head;
}