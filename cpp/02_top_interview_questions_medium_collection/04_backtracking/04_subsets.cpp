class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> power_set = {{}};
        
        for(int num : nums) {
            int n = power_set.size();
            for(int i = 0; i < n; i++) {
                power_set.push_back(power_set[i]);
                power_set.back().push_back(num);
            }
        }
        
        return power_set;
    }
};