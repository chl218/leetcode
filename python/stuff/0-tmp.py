class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        print(nums)
        
        if len(nums) <= 1:
            return [-1, -1]
        
        
        mid = len(nums) // 2
        
        if nums[mid] == target:
            if mid == 0:
                return [mid, mid+1]
            
            if mid == len(nums) - 1:
                return [mid-1, mid]
            
            if nums[mid-1] == target:
                return [mid-1, mid]
            else:
                return [mid, mid+1]
            
            
        if nums[mid] > target:
            return self.searchRange(nums[mid+1:], target)
        else:
            return self.searchRange(nums[:mid], target)
        
        
        