/**

Given an array of integers nums sorted in ascending order, find the starting and
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]


Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

**/


class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if(nums.empty()) {
            return vector<int>(2, -1);
        }
        
        int b = 0;
        int e = nums.size() - 1;        
        int m = e/2;

        while(b != m && e != m) {
            if(nums[m] < target) {
                b = m+1;
            }
            else if(nums[m] > target) {
                e = m-1;
            }
            else {
                b = e = m;
                break;
            }
            m = b + (e - b) / 2;
        }
        
        if(nums[b] != target && nums[e] != target) {
            return vector<int>(2, -1);
        }
        
        while(nums[b] == target && b >= 0) {
            b--;
        }

        int len = nums.size();
        while(nums[e] == target && e < len) {
            e++;
        }
        
        vector<int> res;
        res.push_back(++b);
        res.push_back(--e);
        return res;
    }
};