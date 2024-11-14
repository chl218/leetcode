class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        def bst(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        nums.sort()
        res = 0
        for i in range(len(nums)):
            low  = bst(i+1, len(nums) - 1, lower - nums[i])
            high = bst(i+1, len(nums) - 1, upper - nums[i] + 1)

            res += high - low

        return res