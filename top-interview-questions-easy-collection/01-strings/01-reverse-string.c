/*
 * Write a function that takes a string as input and returns the string 
 * reversed.
 *
 * Example:
 * Given s = "hello", return "olleh".
 *
 **/

char* reverseString(char* s) {
    int len = strlen(s);
    
    char *rs = (char*) malloc(sizeof(char) * len+1);
    char *p = rs;
    
    len--;
    while(len >= 0) {
        *p = s[len];
        p++;
        len--;
    }
    *p = '\0';

    return rs;
}