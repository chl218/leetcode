/**

Roman numerals are represented by seven different symbols: I, V, X, L, C, D
and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added
together. Twelve is written as, XII, which is simply X + II. The number twenty
seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written
as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six
instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be
within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3

Example 2:

Input: "IV"
Output: 4

Example 3:

Input: "IX"
Output: 9

Example 4:

Input: "LVIII"
Output: 58

Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994

Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

**/

int romanToInt(char* s) {
    char *p = s, *q = s+1;
    
    int sum = 0;
    
    while(*p) {
        if(*q) {
            if(*p == 'I' && *q == 'V' || *p == 'I' && *q == 'X') {
                // printf("%c%c ", *p, *q);
                sum += *p == 'I' && *q == 'V' ? 4 : 9;
                p++;
            }
            else if(*p == 'X' && *q == 'L' || *p == 'X' && *q == 'C') {
                // printf("%c%c ", *p, *q);
                sum += *p == 'X' && *q == 'L' ? 40 : 90;
                p++;
            }
            else if(*p == 'C' && *q == 'D' || *p == 'C' && *q == 'M') {
                // printf("%c%c ", *p, *q);
                sum += *p == 'C' && *q == 'D' ? 400 : 900;
                p++;
            }
            else {
                // printf("%c ", *p);
                switch(*p) {
                    case 'I': sum += 1;    break;
                    case 'V': sum += 5;    break;
                    case 'X': sum += 10;   break;
                    case 'L': sum += 50;   break;
                    case 'C': sum += 100;  break;
                    case 'D': sum += 500;  break;
                    case 'M': sum += 1000; break;
                } 
            }
            p++;
            q = p+1;
        }
        else{
            switch(*p) {
                case 'I': sum += 1;    break;
                case 'V': sum += 5;    break;
                case 'X': sum += 10;   break;
                case 'L': sum += 50;   break;
                case 'C': sum += 100;  break;
                case 'D': sum += 500;  break;
                case 'M': sum += 1000; break;
            }
            p++;
        }
    }
    
    return sum;
}