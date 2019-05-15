/**

Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters
only.

Example:

Input: "Hello World"
Output: 5

**/

int tokenize(char **s) {
    
    while(**s == ' ') {
        (*s)++;
    }
    
    int length = 0;
    while(**s && **s != ' ') {
        length++;
        (*s)++;
    }
    
    return length;
}

int lengthOfLastWord(char* s) {
    int curr_len = 0;
    while(*s) {
        int len = tokenize(&s);
        if(len > 0) {
            curr_len = len;
        }
    }
    return curr_len;
}
