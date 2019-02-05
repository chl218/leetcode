/**

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

**/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    
    if(root == NULL) {
        return NULL;
    }
    else {
        int lsz = 0, rsz = 0;
        
        
        int* lchild = inorderTraversal(root->left, &lsz);
        int rootval = root->val;
        int* rchild = inorderTraversal(root->right, &rsz);
        
        int *res = (int*)malloc(sizeof(int) * (lsz + rsz + 1));
        *returnSize = 0;
        
        for(int i = 0; i < lsz; i++) {
            res[(*returnSize)++] = lchild[i];   
        }
        
        res[(*returnSize)++] = rootval;
        
        for(int i = 0; i < rsz; i++) {
            res[(*returnSize)++] = rchild[i];   
        }
        
        return res;
    }
}