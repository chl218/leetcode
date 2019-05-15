/**

Given an array, rotate the array to the right by k steps, where k is
non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]

Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways
to solve this problem. Could you do it in-place with O(1) extra space?

**/

void swap(int *nums, int i, int j) {
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
}

void rotate(int* nums, int numsSize, int k) {

    if(numsSize <= 1 || k == 0){
        return;
    }
    
    if(k >= numsSize) {
        k %= numsSize;
    }
    
    // reverse whole array
    int i = 0;
    int j = numsSize-1;
    while(i < j) {
        swap(nums, i++, j--);
    }
    
    // reverse 0 to k-1
    i = 0;
    j = k-1;
    while(i < j) {
        swap(nums, i++, j--);
    }
    
    // reverse k to n
    i = k;
    j = numsSize-1;
    while(i < j) {
        swap(nums, i++, j--);
    }

}