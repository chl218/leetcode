"""
Given a string s, check if it can be constructed by taking a substring of it
and appending multiple copies of the substring together.


Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.


Example 2:
Input: s = "aba"
Output: false


Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


Constraints:
    1 <= s.length <= 104
    s consists of lowercase English letters.

"""





class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        if not s:
            return False

        ss = (s + s)[1:-1]
        return s in ss

"""
Consider a string S="helloworld". Now, given another string T="lloworldhe",
can we figure out if T is a rotated version of S? Yes, we can! We check if S is
a substring of T+T.

Fine. How do we apply that to this problem? We consider every rotation of
string S such that it's rotated by k units [k < len(S)] to the left.
Specifically, we're looking at strings "elloworldh", "lloworldhe",
"loworldhel", etc...

If we have a string that is periodic (i.e. is made up of strings that are the
same and repeat R times), then we can check if the string is equal to some
rotation of itself, and if it is, then we know that the string is periodic.
Checking if S is a sub-string of (S+S)[1:-1] basically checks if the string is
present in a rotation of itself for all values of R such that 0 < R < len(S).
"""