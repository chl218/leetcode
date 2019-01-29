class Solution {
public:
	vector<int> proudctExceptSelf(vector<int>& nums) {
		vector<int> res(nums.size(), 1);
		
		for(int i = 1; i < nums.size(); i++) {
			res[i] = res[i-1] * nums[i-1];
		}

		int rhs = 1;
		for(int i = nums.size()-1; i >= 0; i--) {
			res[i] *= rhs;
			rhs *= nums[i];
		}
	
		return res;
	}
};
