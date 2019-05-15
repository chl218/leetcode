/* Given a string, find the first non-repeating character in it and return it's 
 * index. If it doesn't exist, return -1.
 *
 * Examples:
 * 
 * s = "leetcode"
 * return 0.
 * 
 * s = "loveleetcode",
 * return 2.
 * 
 * Note: You may assume the string contain only lowercase letters.
 *
 **/

int firstUniqChar(char* s) {
    int counter[26] = {0};
    
    char *p = s;
    while(*p != '\0') {
        counter[*p++ - 97]++;
    }
    
    int index = 0;
    while(*s != '\0') {
        if(counter[*s++ - 97] == 1) {
            return index;
        }
        index++;
    }
    
    return -1;
}