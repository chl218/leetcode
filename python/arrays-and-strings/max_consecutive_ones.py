"""
Given a binary array nums, return the maximum number of consecutive 1's in the
array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 
Constraints:
    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxLen = 0

        i, j, n = 0, 0, len(nums)
        while i < n:

            curLen, j = 0, i

            while j < n:
                if nums[j] != 1:
                    break
                curLen += 1
                j += 1

            if curLen > maxLen:
                maxLen = curLen

            i = j + 1

        return maxLen
