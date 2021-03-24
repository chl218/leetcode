"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

   Hide Hint #1
      This is a really easy problem if you decide to use additional memory. For those trying to write an initial
      solution using additional memory, think counters!
   Hide Hint #2
      However, the trick really is to not use any additional space than what is already available to use. Sometimes,
      multiple passes over the input array help find the solution. However, there's an interesting piece of information
      in this problem that makes it easy to re-use the input array itself for the solution.
   Hide Hint #3
      The problem specifies that the numbers in the array will be in the range [1, n] where n is the number of elements
      in the array. Can we use this information and modify the array in-place somehow to find what we need?
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)

        return res
