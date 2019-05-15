/**

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.

**/

#define MAX(A, B) (A > B ? A : B)

// kadane's algorithm

int maxSubArray(int* nums, int numsSize) {
    int glob_max = nums[0];
    int curr_max = nums[0];
    
    for(int i = 1; i < numsSize; i++) {
        curr_max = MAX(nums[i], curr_max + nums[i]);
        if(curr_max > glob_max) {
            glob_max = curr_max;
        }
    }
    
    return glob_max;
}