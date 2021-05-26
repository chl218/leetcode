"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above
it as shown:


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:
    1 <= numRows <= 30

"""
import math


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def nCr(n, r) -> int:
            return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

        res = []
        for n in range(numRows):
            subRes = []
            for r in range(n+1):
                subRes.append(nCr(n, r))
            res.append(subRes)

        return res
