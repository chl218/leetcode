/**

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true

**/

bool isValid(char* s) {
    
    int sz;
    
    char *p = s;
    while(*p) {
        p++;
        sz++;
    }
    if(sz == 0 || sz % 2 != 0) 
        return false;
    
    int top = 0;
    char *stack = (char*)malloc(sizeof(int) * sz);
        
    p = s;
    while(*p) {
        if(*p == '(' || *p == '{' || *p == '[') {
            stack[top++] = *p;
        }
        else {
            char ch = stack[top-1];
            if(ch == '{' && *p == '}') {
                top--;
            }
            else if(ch == '[' && *p == ']') {
                top--;
            }
            else if(ch == '(' && *p == ')') {
                top--;
            }
            else {
                return false;
            }
        }
        p++;   
    }
    
    return top == 0 ? true : false;
}