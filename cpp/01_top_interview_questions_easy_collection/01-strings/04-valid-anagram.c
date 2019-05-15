/*
 * Given two strings s and t , write a function to determine if t is an anagram
 * of s.
 * 
 * Example 1:
 *    Input: s = "anagram", t = "nagaram"
 *    Output: true
 * 
 * Example 2: 
 *    Input: s = "rat", t = "car"
 *    Output: false
 * 
 * Note:
 * You may assume the string contains only lowercase alphabets.
 * 
 * Follow up:
 * What if the inputs contain unicode characters? How would you adapt your
 * solution to such case?
 * 
 */

bool isAnagram(char* s, char* t) {
    int s_table[26] = {0};
    int t_table[26] = {0};
    
    while(*s != '\0') {
        s_table[*s++ - 97]++;
    }
    
    while(*t != '\0') {
        t_table[*t++ - 97]++;
    }
    
    for(int i = 0; i < 26; i++) {
        if(s_table[i] != t_table[i]) {
            return false;
        }
    }
        
    return true;
}