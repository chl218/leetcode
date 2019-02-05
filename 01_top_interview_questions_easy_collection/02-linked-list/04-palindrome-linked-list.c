/**

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?

**/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */



bool recur(struct ListNode **left, struct ListNode *right) {
    if(right == NULL) {
        return true;
    }
    
    bool res = recur(left, right->next);
    if(res == false) {
        return false;
    }
    
    res = (*left)->val == right->val;
    (*left) = (*left)->next;
    return res;
}


bool isPalindrome(struct ListNode* head) {
    return recur(&head, head);    
}