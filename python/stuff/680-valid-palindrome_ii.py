"""
Given a string s, return true if the s can be palindrome after deleting at most
one character from it.


Example 1:
Input: s = "aba"
Output: true


Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.


Example 3:
Input: s = "abc"
Output: false


Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters.

"""

class Solution:
    def validPalindrome(self, s: str) -> bool:

        deleted = False
        i, j = 0, len(s) - 1

        while i < j:

            if s[i] != s[j]:
                if deleted:
                    return False

                deleted = True

                if s[i+1] == s[j] and s[i] == s[j-1]:
                    return self.validPalindrome(s[i+1:j]) or self.validPalindrome(s[i:j-1])

                if s[i+1] == s[j]:
                    i += 1
                elif s[i] == s[j-1]:
                    j -= 1
                else:
                    return False

            i += 1
            j -= 1

        return True


# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         i = 0
#         j = len(s)-1
#         while i < j:
#             if s[i] != s[j]:
#                 delete_i = s[i+1:j+1]
#                 delete_j = s[i:j]
#                 return self._isPalindrome(delete_i) or self._isPalindrome(delete_j)
#             i += 1
#             j -= 1
#         return True
#     def _isPalindrome(self, s):
#         return s == s[::-1]