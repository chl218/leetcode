/**

Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

**/

class Solution {
public:
    string longestPalindrome(string s) {
        if(s.length() < 2) {
            return s;
        }
                
        int maxlen = 0, minstart = 0;
        
        int i = 0;
        while(i < s.length() - maxlen/2) {
            int j = i, k = i;
            
            while (s[k] == s[k + 1] && k < s.length() - 1) {
                k++;
            }
            i = k + 1;
            
            while (j > 0 && k < s.length() - 1 && s[j - 1] == s[k + 1]) {
                j--; k++;
            }
            
            int currlen = k - j + 1;
            if (currlen > maxlen) {
                maxlen = currlen;
                minstart = j;
            }
    
        }
     
        return s.substr(minstart, maxlen);
    }
};