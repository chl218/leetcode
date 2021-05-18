"""

On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row n and index k, return the kth indexed symbol in row n. (The values of k are 1-indexed.) (1 indexed).

Examples:
Input: n = 1, k = 1
Output: 0

Input: n = 2, k = 1
Output: 0

Input: n = 2, k = 2
Output: 1

Input: n = 4, k = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001

Note:

    n will be an integer in the range [1, 30].
    k will be an integer in the range [1, 2n-1].

Hide Hint #1
   Try to represent the current (N, K) in terms of some (N-1, prevK). What is prevK ?
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n == 1:
            return 0

        isEven = k % 2 == 0
        kPrev = k//2 if isEven else k//2 + 1

        val = self.kthGrammar(n-1, kPrev)

        if val == 0:
            return 1 if isEven else 0
        else:
            return 0 if isEven else 1


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        out = 0

        while k > 1:
            out += (k+1) % 2
            k = (k+1) // 2

        return out % 2
