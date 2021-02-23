"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some
characters of the given string. If there are more than one possible results, return the longest word with the smallest
lexicographical order. If there is no possible result, return the empty string.

Example 1:

Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"

Example 2:

Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"

Note:

   - All the strings in the input will only contain lower-case letters.
   - The size of the dictionary won't exceed 1,000.
   - The length of all the strings in the input won't exceed 1,000.
"""


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        def is_subsequence(s1: str, s2: str) -> bool:

            i, s1_len = 0, len(s1)
            j, s2_len = 0, len(s2)

            while i < s1_len and j < s2_len:
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    j += 1

            return i == s1_len

        # sort by length, then by alphabet
        d.sort(key=lambda x: (-len(x), x))

        for word in d:
            if is_subsequence(word, s):
                return word

        return ""
