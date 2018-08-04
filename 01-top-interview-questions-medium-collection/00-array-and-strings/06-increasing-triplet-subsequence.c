/**

Given an unsorted array return whether an increasing subsequence of length 3
exists or not in the array.

Formally the function should:

Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Note: Your algorithm should run in O(n) time complexity and O(1) space
complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true

Example 2:

Input: [5,4,3,2,1]
Output: false

**/


// first find arr[i] < arr[j]
// then find arr[k] s.t. arr[i] < arr[j] < arr[k]

bool increasingTriplet(int* nums, int numsSize) {
 
    int i = INT_MAX,  j = INT_MAX;
    
    for(int k = 0; k < numsSize; k++) {
        if(nums[k] < i){    // find arr[i]
            i = nums[k];
        }           
        else if(nums[k] > i && nums[k] < j) { // find arr[j]
            j = nums[k];
        }
        else if(nums[k] > i && nums[k] > j) { // find arr[k]
            return true;
        }
    }
    return false;
}