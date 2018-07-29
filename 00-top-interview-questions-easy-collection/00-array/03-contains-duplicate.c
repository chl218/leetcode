/**

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

**/

#include <stdlib.h>

// void qsort (void* base, size_t num, size_t size,
// int (*compar)(const void*,const void*));

int compar (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}


bool containsDuplicate(int* nums, int numsSize) {
     qsort ((void*)nums, numsSize, sizeof(int), compar);
    
    for(int i = 0; i < numsSize-1; i++) {
        if(nums[i] == nums[i+1]) {
            return true;
        }
    }
    
    return false;
}