"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4


Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:
    1 <= nums.length <= 104
    -10^4 < nums[i], target < 10^4
    All the integers in nums are unique.
    nums is sorted in ascending order.

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def _search(self, subnums: List[int], idx: int):

            if not subnums or (len(subnums) == 1 and subnums[0] != target):
                return -1

            mid = len(subnums) // 2

            if subnums[mid] == target:
                return mid + idx

            if subnums[mid] > target:
                return _search(self, subnums[:mid], idx)
            else:
                return _search(self, subnums[mid:], idx+mid)

        return _search(self, nums, 0)


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#     n = len(nums)
#     idx = n // 2
#     tmp = -1
#     while idx != tmp:
#         if nums[idx] == target:
#             return idx
#         tmp = idx
#         if target > nums[idx]:
#             idx += (n - idx) // 2
#         else:
#             idx, n = idx // 2, idx
#     return -1