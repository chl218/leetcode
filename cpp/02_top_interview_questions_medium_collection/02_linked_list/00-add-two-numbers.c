/**

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

**/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int carry = 0;
    if(l1 == NULL || l2 == NULL) {
        return NULL;
    }
    
    struct ListNode *res = NULL, *p;
    
    while(l1 && l2) {
        int sum = l1->val + l2->val + carry;
        
        struct ListNode *digit = (struct ListNode*)malloc(sizeof(struct ListNode));
        digit->next = NULL;
        digit->val  = sum%10;
        carry       = sum/10;
        
        if(res) {
            res->next = digit;
            res       = digit;
        }
        else {
            res = digit;
            p   = res;
        }
        
        l1 = l1->next;
        l2 = l2->next;
    }
    

    while(l1) {
        int sum = l1->val + carry;
        
        struct ListNode *digit = (struct ListNode*)malloc(sizeof(struct ListNode));
        digit->next = NULL;
        digit->val  = sum%10;
        carry       = sum/10;
        
        if(res) {
            res->next = digit;
            res       = digit;
        }
        else {
            res = digit;
            p   = res;
        }
        
        l1 = l1->next;
    }
    
    while(l2) {
        int sum = l2->val + carry;
        
        struct ListNode *digit = (struct ListNode*)malloc(sizeof(struct ListNode));
        digit->next = NULL;
        digit->val  = sum%10;
        carry       = sum/10;
        
        if(res) {
            res->next = digit;
            res       = digit;
        }
        else {
            res = digit;
            p   = res;
        }
        l2 = l2->next;
    }
    
    
    if(carry) {
        struct ListNode *digit = (struct ListNode*)malloc(sizeof(struct ListNode));
        digit->next = NULL;
        digit->val  = carry;
        res->next   = digit;
    }
    

    return p;
    
}