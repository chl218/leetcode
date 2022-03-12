

def hammingWeight(n):
    """Number of 1 Bits

    Write a function that takes an unsigned integer and return the number of '1'
    bits it has (also known as the Hamming weight).
    """

    count = 0
    for i in range(32):
        count += (n >> i) & 1
    return count



def combinationSum(candidates, target):
   ret = []
   dfs(candidates, target, [], ret)
   return ret

def dfs(self, nums, target, path, ret):
   if target < 0:
      return
   if target == 0:
      ret.append(path)
      return
   for i in range(len(nums)):
      self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)