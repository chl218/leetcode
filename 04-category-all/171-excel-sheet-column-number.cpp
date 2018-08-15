/**

Given a column title as appear in an Excel sheet, return its corresponding
column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1


Example 2:

Input: "AB"
Output: 28


Example 3:

Input: "ZY"
Output: 701

**/

class Solution {
public:
    int titleToNumber(string s) {
        int idx = s.length()-1;
        
        int depth = 0;
        int sum = 0;
        while(idx >= 0) {
            int pos = s[idx--] - 'A' + 1;
            // printf("%c %d\n", s[idx], pos);
            sum += pos * pow(26, depth++);
        }
        
        return sum;
    }
};