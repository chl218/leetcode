class Solution:
    def jump(self, nums: List[int]) -> int:
        position = 0
        steps = 0
        while position < len(nums)-1:
            steps += 1
            position = self.nextposition(nums,position)
        return steps

    
    def nextposition(self, nums: List[int], n: int) -> int:
        nextposition = n
        farestposition = n+nums[n]
        if farestposition >= len(nums)-1:
            return len(nums)-1
        else:
            for i in range(1,nums[n]+1):
                if n+i+nums[n+i] > farestposition:
                    nextposition = n+i
                    farestposition = n+i+nums[n+i]
            return nextposition