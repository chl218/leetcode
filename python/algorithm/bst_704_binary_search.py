class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        idx = n // 2
        tmp = -1

        while idx != tmp:

            if nums[idx] == target:
                return idx

            tmp = idx
            if target > nums[idx]:
                idx += (n - idx) // 2
            else:
                idx, n = idx // 2, idx

        return -1


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         lo, hi = 0, len(nums) - 1
#         while lo <= hi:
#             middle = (lo + hi) // 2
#             if nums[middle] == target:
#                 return middle
#             elif nums[middle] > target:
#                 hi = middle - 1
#             else:
#                 lo = middle + 1
#         return -1

