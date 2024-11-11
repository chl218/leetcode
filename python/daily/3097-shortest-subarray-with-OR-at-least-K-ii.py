""" 3097. Shortest Subarray With OR at Least K II

You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

 
Example 1:
Input: nums = [1,2,3], k = 2
Output: 1
Explanation:
The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:
Input: nums = [2,1,8], k = 10
Output: 3
Explanation:
The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:
Input: nums = [1,2], k = 0
Output: 1
Explanation:
The subarray [1] has OR value of 1. Hence, we return 1.

Constraints:

    1 <= nums.length <= 2 * 105
    0 <= nums[i] <= 109
    0 <= k <= 109

"""

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        res = float('inf')
        bit_map = [0] * 32

        def update_bit_map(bm, n, diff):
            for i in range(32):
                if n & (1 << i):
                    bm[i] += diff

        def bits_to_int(bm):
            res = 0
            for i in range(32):
                if bm[i]:
                    res = res | (1 << i)
            return res

        lhs = 0
        for rhs in range(len(nums)):
            
            update_bit_map(bit_map, nums[rhs], 1)
            current_OR_val = bits_to_int(bit_map)

            while lhs <= rhs and current_OR_val >= k:
                res = min(res, rhs - lhs + 1)
                update_bit_map(bit_map, nums[lhs], -1)
                current_OR_val = bits_to_int(bit_map)
                lhs += 1

        return -1 if res == float('inf') else res
