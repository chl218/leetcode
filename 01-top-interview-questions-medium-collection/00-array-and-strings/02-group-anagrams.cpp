/**

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

All inputs will be in lowercase.
The order of your output does not matter.

**/


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string> > hash;
        
        for(int i = 0; i < strs.size(); i++) {
            string idx = strs[i];
            sort(idx.begin(), idx.end());
            hash[idx].push_back(strs[i]);   
        }
        
        vector<vector<string> > res;
        for(unordered_map<string, vector<string> >::iterator it = hash.begin(); it != hash.end(); it++) {
            vector<string>::iterator b = it->second.begin();
            vector<string>::iterator e = it->second.end();
            
            vector<string> lst;
            while(b != e) {
                lst.push_back(*b);
                b++;
            }
            res.push_back(lst);
            
                
        }
        
        return res;
    }
};