
/**

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".

Example 1:

    Input: ["flower","flow","flight"]
    Output: "fl"

Example 2:

    Input: ["dog","racecar","car"]
    Output: ""

Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

**/

#define PREFIX_SZ sizeof(char) * 128

char* longestCommonPrefix(char** strs, int strsSize) {

    int max_sz = INT_MAX;
    for(int i = 0; i < strsSize; i++){
        int len = strlen(strs[i]); 
        if(len < max_sz) {
            max_sz = len;
        }
    }
    
    char* prefix = (char*) malloc(PREFIX_SZ);
    memset(prefix, '\0', sizeof(char) * PREFIX_SZ);    
    
    if(max_sz == 0 || max_sz == INT_MAX) {
        return prefix;
    }
    
    char* word = *strs;
    char  ch   = *word;
    
    int index = 0;
    while(index < max_sz) {

        for(int i = 1; i < strsSize; i++) {
            if(ch != (strs[i])[index]) {
                return prefix;
            }
        }
        
        prefix[index++] = ch;
        ch = *(++word);        
    }
    
    return prefix;
}