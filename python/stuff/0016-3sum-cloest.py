"""
3Sum Closest

Given an integer array nums of length n and an integer target, find three
integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.


Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Example 2:
Input: nums = [0,0,0], target = 1
Output: 0

Constraints:
    3 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    -10^4 <= target <= 10^4
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            l, r = i + 1, n - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if abs(ans - target) > abs(sum3 - target):
                    ans = sum3
                if sum3 == target: return target
                if sum3 > target:
                    r -= 1  # Sum3 is greater than the target, to minimize the difference, we have to decrease our sum3
                else:
                    l += 1  # Sum3 is lesser than the target, to minimize the difference, we have to increase our sum3
        return ans