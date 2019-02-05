/**

Given a binary tree, return the bottom-up level order traversal of its nodes'
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        
        if(root == NULL) {
            return std::vector< std::vector<int> >();
        }
        
        std::list<vector<int> > lst;
        
        std::queue<TreeNode *> lqueue;
        
        lqueue.push(root);
        
        while(!lqueue.empty()) {
            std::vector<int> curr_level;
            int nodes = lqueue.size();
                
            while(nodes > 0) {
                TreeNode *node = lqueue.front(); lqueue.pop();
                
                curr_level.push_back(node->val);
                
                if(node->left)  lqueue.push(node->left);
                if(node->right) lqueue.push(node->right);
                
                nodes--;
            }
            
            lst.push_front(curr_level);
        }
        
        std::vector< std::vector<int> > res;
        for(auto obj : lst) {
            res.push_back(obj);
        }
        
        return res;
    }
};