"""
Given an array of strings words, return the words that can be typed using
letters of the alphabet on only one row of American keyboard like the imagbelow.

In the American keyboard:
    the first row consists of the characters "qwertyuiop",
    the second row consists of the characters "asdfghjkl", and
    the third row consists of the characters "zxcvbnm".


Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]


Example 2:
Input: words = ["omk"]
Output: []


Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]


Constraints:
    1 <= words.length <= 20
    1 <= words[i].length <= 100
    words[i] consists of English letters (both lowercase and uppercase).

"""

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

        filtered = []
        for row in rows:
            for word in words:
                valid = True
                for letter in word.lower():
                    if letter not in row:
                        valid = False
                        break

                if valid:
                    filtered.append(word)

        return filtered