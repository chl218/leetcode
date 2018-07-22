/**
Given two arrays, write a function to compute their intersection.

Example:

Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both
arrays. The result can be in any order.

Follow up:

What if the given array is already sorted? How would you optimize your
algorithm?

What if nums1's size is small compared to nums2's size? Which algorithm is
better?

What if elements of nums2 are stored on disk, and the memory is limited such
that you cannot load all elements into the memory at once?


**/

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    
    int size = nums1Size < nums2Size ? nums1Size : nums2Size;
    int *arr  = (int*)malloc(sizeof(int) * size);    
    int *skip = (int*)malloc(sizeof(int) * size);    

    *returnSize = 0;
    
    for(int i = 0; i < nums2Size; i++) {
        for(int j = 0; j < nums1Size; j++) {
            if(nums2[i] == nums1[j]) {
                
                int flag = 1;
                for(int k = 0; k < *returnSize; k++) {
                    if(skip[k] == j) {
                        flag = 0;
                    }
                }
                
                if(flag) {
                    arr[*returnSize] = nums2[i];
                    skip[*returnSize] = j;
                    (*returnSize)++;
                    break;
                }    
            }
        }
    }
    return arr;
}