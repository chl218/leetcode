/**

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.



**/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int minDepth(struct TreeNode* root) {
    if(!root) {
        return 0;
    }
    else {
        int lst = minDepth(root->left);
        int rst = minDepth(root->right);
        
        if(!root->left) {
            return ++rst;
        }
        if(!root->right) {
            return ++lst;
        }
        
        return lst < rst ? ++lst : ++rst;
    }
}