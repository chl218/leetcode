"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to
get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character, but a character may map to itself.

 
Example 1:
Input: s = "egg", t = "add"
Output: true


Example 2:
Input: s = "foo", t = "bar"
Output: false


Example 3:
Input: s = "paper", t = "title"
Output: true
 

Constraints:
    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        h1 = {}
        h2 = {}

        for c1, c2 in zip(s, t):

            if c1 not in h1:
                h1[c1] = c2
            else:
                if not h1[c1] == c2:
                    return False

            if c2 not in h2:
                h2[c2] = c1
            else:
                if not h2[c2] == c1:
                    return False

        return True
