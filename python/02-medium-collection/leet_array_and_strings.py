from typing import List

def threeSum(self, nums: List[int]) -> List[List[int]]:
    """3 Sums

    Given an array nums of n integers, are there elements a, b, c in nums such
    that a + b + c = 0? Find all unique triplets in the array which gives the
    sum of zero.

    Note:
        - The solution set must not contain duplicate triplets.

    Example:
        Given array nums = [-1, 0, 1, 2, -1, -4]
        A solution set is: [[-1, 0, 1], [-1, -1, 2]]
    """
    
    res = []
    nums.sort()
    
    if nums[0] > 0 or nums[-1] < 0:
        return res
    
    for i in range(0, len(nums)-2):
        
        # Sum will always be creater than 0
        if nums[i] > 0:
            return res
        
        # Duplicate guard
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        j = i + 1
        k = len(nums) - 1

        while j < k:
            _3sum = nums[i] + nums[j] + nums[k] 
            if _3sum == 0:
                res.append([nums[i], nums[j], nums[k]])

                # Get all other matching conditions
                while j < k and nums[j] == nums[j+1]: j += 1
                while k > j and nums[k] == nums[k-1]: k -= 1
                j += 1
                k -= 1
            elif _3sum > 0:
                k -= 1
            else:
                j += 1

    return res    


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    """Group Anagrams

    Given an array of strings, group anagrams together.

    Example:
        Input:  ["eat", "tea", "tan", "ate", "nat", "bat"],
        Output: [["ate","eat","tea"], ["nat","tan"], ["bat"]]

    Note:
        - All inputs will be in lowercase.
        - The order of your output does not matter.
    """
    lst = []
    dic = {}
    idx = 0
    
    for word in strs:
        key = ''.join(sorted(word))
        
        if key in dic:
            lst[dic[key]].append(word)
        else:
            lst.append([word])
            dic[key] = idx
            idx += 1
            
    return lst