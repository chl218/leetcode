/**

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

**/

class Solution {
public:
    string addBinary(string a, string b) {
        int lenA = a.length()-1;
        int lenB = b.length()-1;
        
        int idx = lenA > lenB ? lenA + 2 : lenB + 2;
        string res(idx--, ' ');
        
        
        int carry = 0;
        while(lenA >= 0 && lenB >= 0) {
            int sum = (a[lenA] - '0') + (b[lenB] - '0') + carry;
            
            switch(sum) {
                case 3: 
                    res[idx--] = '1';
                    carry    = 1;
                    break;
                case 2:
                    res[idx--] = '0';
                    carry    = 1;
                    break;
                default:
                    res[idx--] = sum + '0';
                    carry    = 0;
            }
            lenA--;
            lenB--;
        }
        
        while(lenA >= 0) {
            int sum = (a[lenA] - '0') + carry;
            
            if(sum == 2) {
                res[idx--] = '0';
                carry = 1;
            }
            else {
                res[idx--] = sum + '0';
                carry = 0;
            }
            
            lenA--;
        }
        
        while(lenB >= 0) {
            int sum = (b[lenB] - '0') + carry;
            if(sum == 2) {
                res[idx--] = '0';
                carry = 1;
            }
            else {
                res[idx--] = sum + '0';
                carry = 0;
            }
            lenB--;
        }
        
        if(carry) {
            res[0] = '1';
            return res;
        }
        else {
            return std::string(res.begin()+1, res.end());
        }
      
    }
};