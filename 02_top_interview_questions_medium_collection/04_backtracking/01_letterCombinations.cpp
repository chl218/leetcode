class Solution {

public:
    vector<string> letterCombinations(string digits) {
        
        if(digits.size() == 0) {
            return vector<string>();
        }
        
        vector<string> map = {"","", "abc", "def", "ghi", "jkl", 
                                "mno", "pqrs", "tuv", "wxyz"};
        
        vector<string> result;
        result.push_back("");
        
        for(auto digit : digits) {
            string candidates = map[digit - '0'];
            vector<string> tmp;
            for(auto candidate : candidates) {
                for(auto substr : result) {
                    tmp.push_back(substr + candidate);
                }
            }
            result.swap(tmp);
        }
    
        return result;
    }

};