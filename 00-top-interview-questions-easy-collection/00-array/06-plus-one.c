/**

Given a non-empty array of digits representing a non-negative integer, plus one
to the integer.

The digits are stored such that the most significant digit is at the head of the
list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]

Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]

Explanation: The array represents the integer 4321.


**/


/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
 
    
    int *arr = (int*) malloc(sizeof(int) * (digitsSize + 1));
    
    *returnSize = digitsSize;
    
    int carry = 1;
    for(int i = digitsSize-1; i >= 0; i--) {
        int val = digits[i] + carry;
        
        if(val > 9) {
            arr[i+1] = 0;
            carry = 1;
        }
        else{
            arr[i+1] = val;
            carry = 0;
        }
    }
    
    if(carry == 1) {
        arr[0] = 1;
        *returnSize += 1;
    }
    else {
        memmove(arr, arr+1, sizeof(int)*(*returnSize));
    }
    
    return arr;
}