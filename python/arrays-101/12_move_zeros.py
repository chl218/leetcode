"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = j = 0
        n = len(nums)
        while i < n and j < n:
            if nums[i] == 0:
                while j < n and nums[j] == 0:
                    j += 1

                if j == n:
                    return

                nums[i] = nums[j]
                nums[j] = 0

                i += 1
            else:
                i += 1
                j = i
