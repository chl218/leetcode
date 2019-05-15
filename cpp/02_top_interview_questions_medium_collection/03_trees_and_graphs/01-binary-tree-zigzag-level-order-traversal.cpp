/**

Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        queue<TreeNode *> lvlqueue;
        vector<vector<int> > res;
        
        int parity = 2;
        
        if(root == NULL) {
            return res;
        }
        
        lvlqueue.push(root);
        
        while(!lvlqueue.empty()) {
            list<int> lst;
            
            int size = lvlqueue.size();
            while(size) {
                TreeNode *node = lvlqueue.front(); lvlqueue.pop();
                
                if(parity % 2 == 0) {
                    lst.push_back(node->val);
                }
                else {
                    lst.push_front(node->val);
                }
                
                if(node->left)  lvlqueue.push(node->left);
                if(node->right) lvlqueue.push(node->right);
                
                size--;
            }
            parity++;
            
            vector<int> currlvl(begin(lst), end(lst));
            res.push_back(currlvl);
        }
        
        return res;
    }
};