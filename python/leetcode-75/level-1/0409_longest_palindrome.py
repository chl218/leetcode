"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the
length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome
here.


Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose
length is 7.


Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.


Constraints:
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.

"""

class Solution:
    def longestPalindrome(self, s: str) -> int:

        hmap = {}
        for c in s:
            if c not in hmap:
                hmap[c] = 1
            else:
                hmap[c] += 1

        maxLen = 0
        hasOdd = False
        for key, val in hmap.items():

            if val % 2 == 0:
                maxLen += val
            else:
                hasOdd = True
                maxLen += (val - 1)

        return maxLen if not hasOdd else maxLen+1


# def longestPalindrome_set(s):
#        ss = set()
#     for letter in s:
#         if letter not in ss:
#             ss.add(letter)
#         else:
#             ss.remove(letter)
#     if len(ss) != 0:
#         return len(s) - len(ss) + 1
#     else:
#         return len(s)