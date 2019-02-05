/**

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

**/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {

    if(root == NULL) {
        return 0;
    }
    else {
        int ldepth = maxDepth(root->left);
        int rdepth = maxDepth(root->right);
        
        return ldepth > rdepth ? ldepth+1 : rdepth+1;
    }
}