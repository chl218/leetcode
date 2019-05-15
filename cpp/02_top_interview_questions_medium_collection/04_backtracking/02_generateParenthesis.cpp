class Solution {
public:
    
    void backtrack(string str, int left, int right, vector<string> &res) {
        
        if(left == 0 && right == 0) {
            res.push_back(str);
            return;
        }
        
        if(left > 0) {
            backtrack(str+"(", left-1, right, res);
        }
        
        if(left < right) {
            backtrack(str+")", left, right-1, res);
        }
        
    }
    
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        backtrack("", n, n, res);      
        return res;
    }
};