"""
Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return
the maximum number.



Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.

Example 2:

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.



Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1


Follow up: Can you find an O(n) solution?
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        res = [float('-inf'), float('-inf'), float('-inf')]

        for num in nums:
            if num not in res:
                if num > res[0]:
                    res = [num, res[0], res[1]]
                elif num > res[1]:
                    res = [res[0], num, res[1]]
                elif num > res[2]:
                    res = [res[0], res[1], num]

        return max(nums) if float('-inf') in res else res[2]
