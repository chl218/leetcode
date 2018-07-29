/**

Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of
zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

**/

/**
 * Return an array of arrays of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}


int** threeSum(int* nums, int numsSize, int* returnSize) {
    qsort((void*)nums, numsSize, sizeof(int), cmpfunc);


    int **res = (int**)malloc(sizeof(int*) * numsSize*numsSize);
    int   idx = 0;
    
    for(int i = 0; i < numsSize - 2; i++) {
        int a = nums[i];
        if(i > 0 && a == nums[i-1]) {
            continue;
        }
        
        int beg = i+1;
        int end = numsSize-1;
        
        while(beg < end) {
            int b = nums[beg];
            int c = nums[end];
            
            if(a+b+c == 0) {
                int *list = (int*)malloc(sizeof(int) * 3);
                list[0] = a;
                list[1] = b;
                list[2] = c;
                res[idx++] = list;
                
                while(beg < end && b == nums[beg]) {
                    beg++;
                }
                while(end > beg && c == nums[end]) {
                    end--;
                }
            }
            else if(a+b+c < 0) {
                beg++;
            }
            else {
                end--;   
            }
            
        } //end-while
    } //end-for
    
    
    
    *returnSize = idx;
    return res;
    
}