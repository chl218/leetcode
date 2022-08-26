"""
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed
into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.


Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".


Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".


Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:
    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        sstack = []
        tstack = []

        for ss in s:

            if ss == '#':
                if sstack:
                    sstack.pop()
            else:
                sstack.append(ss)


        for tt in t:
            if tt == '#':
                if tstack:
                    tstack.pop()
            else:
                tstack.append(tt)

        return sstack == tstack

#
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#     def helper(s):
#         s = list(s)
#         ans = []
#         for c in s:
#             if c == "#":
#                 if ans:
#                     ans.pop()
#             else:
#                 ans.append(c)
#         return "".join(ans)

#     return helper(s) == helper(t)