/**

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the
array's size.

**/

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        // record frequency
        unordered_map<int, int> hash;
        for(int n : nums) {
            hash[n]++;
        }
    

        // bucket sort frequency, using frequency count as index, and
        // frequency number as value
        vector<vector<int> > bucket(nums.size() + 1, vector<int>{});
        for(auto it : hash) {
            bucket[it.second].push_back(it.first);
        }
       
        // search bucket from highest frequency/index, to get the value
        vector<int> res;
        for(int i = bucket.size() - 1; i > 0; i--) {
            for(int n : bucket[i]) {
                res.push_back(n);
            }
            
            if(res.size() == k) {
                break;
            }
        }
        
        return res;
    }
};