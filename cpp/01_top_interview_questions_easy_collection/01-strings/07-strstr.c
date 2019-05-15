/**
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().

**/

int strStr(char* haystack, char* needle) {
    
    int hlen = strlen(haystack);
    int nlen = strlen(needle);
    
    if(nlen == 0) {
        return 0;
    }
    if(nlen > hlen) {
        return -1;
    }
    
    char* hptr = haystack;
    char* nptr = needle;
    
    int hindex = 0;
    while(hptr != '\0' && (hindex + nlen <= hlen)){
        int matched = 1;
        for(int i = hindex, j = 0; i < hindex+nlen; i++, j++) {
            if(haystack[i] != needle[j]) {
                matched = 0;
                break;
            } 
        }
        if(matched) {
            return hindex;
        }
        
        hindex++;
        hptr++;
    }
    
    return -1;
}