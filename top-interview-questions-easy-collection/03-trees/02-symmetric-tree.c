/**

Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.

**/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool aux(struct TreeNode *lroot, struct TreeNode *rroot) {
    if(lroot == NULL && rroot == NULL) {
        return true;
    }
    
    if(lroot != NULL && rroot != NULL && lroot->val != rroot->val ||
       lroot == NULL && rroot != NULL                             ||
       lroot != NULL && rroot == NULL) {
        return false;
    }
    
    return aux(lroot->left, rroot->right) && aux(lroot->right, rroot->left);
    
}

bool isSymmetric(struct TreeNode* root) {
    if(root == NULL) return true;
    
    return aux(root->left, root->right);
    
}