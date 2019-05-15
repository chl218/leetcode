/**

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and
for the multiples of five output “Buzz”. For numbers which are multiples of
both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

**/

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** fizzBuzz(int n, int* returnSize) {
 
    char **arr = (char**)malloc(sizeof(char*) * n);
    
    *returnSize = 0;
    
    for(int i = 1; i <= n; i++) {
        (*returnSize)++;
        if(i % 3 == 0 && i % 5 == 0) {
            char *fb = (char*)malloc(sizeof(char) * 9);
            strcpy(fb, "FizzBuzz");
            arr[i-1] = fb;
        }
        else if(i % 3 == 0) {
            char *f = (char*)malloc(sizeof(char) * 5);
            strcpy(f, "Fizz");
            arr[i-1] = f;
        }
        else if(i % 5 == 0) {
            char *b = (char*)malloc(sizeof(char) * 5);
            strcpy(b, "Buzz");
            arr[i-1] = b;
        }
        else {
            int val = i;
            int len = 0;
            while(val > 0) {
                val = val/10;
                len++;
            }
            
            char *str = (char*)malloc(sizeof(char) * len+1);
            memset(str, '\0', len+1);
            
            val = i;
            while(val > 0) {
                str[--len] = (val%10) + '0';
                val = val/10;
            }
            arr[i-1] = str;
        }
    }
    
    return arr;
}