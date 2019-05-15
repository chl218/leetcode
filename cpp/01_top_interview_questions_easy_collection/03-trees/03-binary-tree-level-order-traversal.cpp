/**

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

**/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        
        queue<TreeNode *> lqueue;
        vector<vector<int>> res;

        
        if(root == NULL) {
            return res;            
        }
        
        lqueue.push(root);
        
        while(!lqueue.empty()) {
            vector<int> currLevel;
            int size = lqueue.size();
            
            while(size) {
                TreeNode *node = lqueue.front(); lqueue.pop();
                currLevel.push_back(node->val);
                
                if(node->left)  lqueue.push(node->left);
                if(node->right) lqueue.push(node->right);
                
                size--;
            }
            
            res.push_back(currLevel);
        }
        
        return res;
    }
};