"""
An integer array is called arithmetic if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.

Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and
             [1,2,3,4] itself.


Example 2:
Input: nums = [1]
Output: 0


Constraints:
    1 <= nums.length <= 5000
    -1000 <= nums[i] <= 100

"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        n = len(nums)

        if n < 3:
            return 0

        len_window = n
        subarray = 0
        while len_window >= 3:

            for i in range(n - len_window + 1):

                j = i+1
                subcount = 0
                diff = nums[j-1] - nums[j]
                while j < i + len_window:
                    if nums[j-1] - nums[j] == diff:
                        subcount += 1
                        j += 1
                    else:
                        break

                if subcount == len_window - 1:
                    subarray += 1

            len_window -= 1

        return subarray



# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         cons = 0
#         res = 0
#         for i in range(2, len(nums)):
#             if nums[i] + nums[i-2] == 2 * nums[i-1]:
#                 cons += 1
#             else:
#                 cons = 0
#             res += cons
#         return res