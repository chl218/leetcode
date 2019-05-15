/**

Given an array where elements are sorted in ascending order, convert it to a
height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following
height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if(nums.size() == 0) {
            return NULL;
        }
        
        int mid = nums.size()/2;
        int end = nums.size() - 1;
        
        // printf("%d %d\t", mid, end);
        
        TreeNode *root = (TreeNode*)malloc(sizeof(TreeNode));
        root->val = nums[mid];
        
        vector<int> left;
        for(int i = 0; i < mid; i++) {
            left.push_back(nums[i]);
        }
        
        vector<int> right;
        for(int i = mid+1; i <= end; i++) {
            right.push_back(nums[i]);
        }
        
        // printf("%d %d\n", left.size(), right.size());
        
        root->left  = sortedArrayToBST(left);
        root->right = sortedArrayToBST(right);
        
        return root;
    }
};