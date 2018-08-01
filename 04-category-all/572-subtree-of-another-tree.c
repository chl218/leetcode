/**

Given two non-empty binary trees s and t, check whether tree t has exactly the
same structure and node values with a subtree of s. A subtree of s is a tree
consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.

Example 1:

Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:
   4 
  / \
 1   2

Return true, because t has the same structure and node values with a subtree
of s.



Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:
   4
  / \
 1   2

Return false.

**/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool equals(struct TreeNode *s, struct TreeNode *t) {
    if(s == NULL && t == NULL) {
        return true;
    }
    if(s == NULL || t == NULL) {
        return false;
    }
    
    return (s->val == t->val) && equals(s->right, t->right) 
                              && equals(s->left, t->left);
}


bool isSubtree(struct TreeNode* s, struct TreeNode* t) {
    return s != NULL && (equals(s, t) || isSubtree(s->right, t)
                                      || isSubtree(s->left, t));   
}