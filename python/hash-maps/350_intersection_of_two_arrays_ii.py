"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear
as many times as it shows in both arrays and you may return the result in any order.


Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:
   1 <= nums1.length, nums2.length <= 1000
   0 <= nums1[i], nums2[i] <= 1000



Follow up:

   What if the given array is already sorted? How would you optimize your algorithm?
   What if nums1's size is small compared to nums2's size? Which algorithm is better?
   What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into
   the memory at once?

"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        h1 = Counter(nums1)
        h2 = Counter(nums2)

        res = []
        counts = h1 if len(h1) > len(h2) else h2
        for val in counts:
            if val in h1 and val in h2:
                amt = h1[val] if h1[val] < h2[val] else h2[val]
                res.extend([val] * amt)

        return res

# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         c = Counter(nums1)
#         output = []
#         for n in nums2:
#             if c[n] > 0:
#                 output.append(n)
#                 c[n]-=1

#         return output