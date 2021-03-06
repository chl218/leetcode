/**

Given a positive integer, return its corresponding column title as appear in an
Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"

Example 2:

Input: 28
Output: "AB"

Example 3:

Input: 701
Output: "ZY"

**/

class Solution {
public:
    string convertToTitle(int n) {
      char table[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G',
                      'H', 'I', 'J', 'K', 'L', 'M', 'N', 
                      'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                      'V', 'W', 'X', 'Y', 'Z' };
        
        string res = "";
        
        while(n > 0) {
            res = table[(n-1) % 26] + res;            
            n = (n-1) / 26;
        }
        
        return res;
    }
};