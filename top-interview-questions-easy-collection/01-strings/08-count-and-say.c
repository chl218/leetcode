/**

The count-and-say sequence is the sequence of integers with the first five terms
as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"





**/

#define MAX_LENGTH 2048 * 10

char* countAndSay(int n) {

    static char scratch_mem[MAX_LENGTH];
    
    if(n == 1) {
        char* c = (char*)malloc(sizeof(char) << 1);
        memset(c, '\0', sizeof(char) << 1);
        *c = '1';
        return c;
    }
    else {
        char* str = countAndSay(n - 1);
        char* ptr = str;
        
        int index = 0;
        char* res = (char*) malloc(sizeof(char) * MAX_LENGTH);        
        memset(res, '\0', sizeof(char) * MAX_LENGTH);
        
        int num     = *ptr - '0';
        int num_cnt = 1;
        while(*ptr != '\0') {            
            ptr++;
            if((*ptr - '0') != num) {
                int i = 0;
            
                scratch_mem[i++] = num + '0';
                while(num_cnt > 0) {
                    scratch_mem[i++] = (num_cnt % 10) + '0';
                    num_cnt          = num_cnt/10;
                }


                for(int j = i-1; j >= 0; j--) {
                    res[index++] = scratch_mem[j];
                }
                
                num     = *ptr - '0';
                num_cnt = 0;
                
            } // end-if
            num_cnt++;
        } // end-while
        free(str);
        return res;
    } // end-else
}