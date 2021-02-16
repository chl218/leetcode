"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hmap = {}

        for i in range(len(s)):
            if s[i] not in hmap:
                hmap[s[i]] = 1
            else:
                hmap[s[i]] += 1

            if t[i] not in hmap:
                hmap[t[i]] = -1
            else:
                hmap[t[i]] -= 1

        for k in hmap.keys():
            if hmap[k] != 0:
                return False

        return True
