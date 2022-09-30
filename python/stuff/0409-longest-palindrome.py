"""
Given a string s which consists of lowercase or uppercase letters, return the
length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome
here.


Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.


Example 2:
Input: s = "a"
Output: 1


Example 3:
Input: s = "bb"
Output: 2


Constraints:
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.

"""

class Solution:
    def longestPalindrome(self, s: str) -> int:

        cmap = {}
        for c in s:
            if c not in cmap:
                cmap[c] = 1
            else:
                cmap[c] += 1

        count = 0
        left_over = False
        for val in cmap.values():
            if val % 2 == 0:
                count += val
            else:
                left_over = True
                count += (val - 1)

        return count if not left_over else count + 1


# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         odd_chars = set()
#         max_len = 0
#         for char in s:
#             if char not in odd_chars:
#                 odd_chars.add(char)
#             else:
#                 odd_chars.remove(char)
#                 max_len += 2
#         if len(odd_chars) >= 1:
#             max_len += 1
#         return max_len