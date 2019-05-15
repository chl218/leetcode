/**

Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

**/

void moveZeroes(int* nums, int numsSize) {
     
    int i = 0, j = 1;
        
    while(j < numsSize) {
        if(nums[i] == 0) {
            while(nums[j] == 0) {
                j++;
                if(j == numsSize) {
                    return;
                }
            }
            nums[i] = nums[j];
            nums[j] = 0;
        }
        i++;
        j++;
    }
    
}