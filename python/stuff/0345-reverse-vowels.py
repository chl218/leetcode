"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.


Example 1:
Input: s = "hello"
Output: "holle"


Example 2:
Input: s = "leetcode"
Output: "leotcede"


Constraints:
    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.

"""

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        b, e = 0, len(s)-1
        slst = [c for c in s]

        while b < e:
            if s[b] in vowels and s[e] in vowels:
                slst[b], slst[e] = slst[e], slst[b]
                b += 1
                e -= 1
            elif s[b] in vowels:
                e -= 1
            elif s[e] in vowels:
                b += 1
            else:
                b += 1
                e -= 1

        return ''.join(slst)