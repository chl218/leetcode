"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in s.



Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true


Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false


Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:
    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.

"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:


        pattern_list = [c for c in pattern]
        str_list = s.split(' ')

        if len(pattern_list) != len(str_list):
            return False


        ab_map = {}
        ba_map = {}
        for a, b in zip(pattern_list, str_list):

            if a not in ab_map and b not in ba_map:
                ab_map[a] = b
                ba_map[b] = a
            elif a in ab_map and b in ba_map:
                if ab_map[a] != b or ba_map[b] != a:
                    return False
            else:
                return False

        return True
