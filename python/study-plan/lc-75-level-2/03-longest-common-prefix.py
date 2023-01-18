"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

"""

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            oldprefix = prefix

            for i in range(min(len(prefix), len(word))):
                if prefix[i] != word[i]:
                    prefix = prefix[:i]
                    break

            if prefix == oldprefix and len(word) < len(prefix):
                prefix = word

        return prefix
