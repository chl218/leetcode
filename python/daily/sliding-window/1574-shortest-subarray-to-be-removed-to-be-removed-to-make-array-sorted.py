class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        N = len(arr)
        left, right = 0, N - 1

        while left + 1 < N and arr[left] <= arr[left+1]:
            left += 1

        if left == N - 1:
            return 0

        while right > 0 and arr[right-1] <= arr[right]:
            right -= 1

        res = min(N - left - 1, right)

        i, j = 0, right
        while i <= left and j < N:
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1

        return res