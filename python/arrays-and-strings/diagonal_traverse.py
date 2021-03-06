"""
Given an m x n matrix mat, return an array of all the elements of the array in
a diagonal order.

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 
Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 104
    1 <= m * n <= 104
    -105 <= mat[i][j] <= 105
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m, n = len(mat), len(mat[0])
        i, j = 0, 0
        res = [0] * m * n
        upDirection = True

        for idx in range(m*n):

            res[idx] = mat[i][j]

            if upDirection:
                if i > 0 and j < n-1:
                    i -= 1
                    j += 1
                elif j == n-1:
                    i += 1
                    upDirection = False
                elif i == 0:
                    j += 1
                    upDirection = False
            else:
                if i < m-1 and j > 0:
                    i += 1
                    j -= 1
                elif i == m-1:
                    j += 1
                    upDirection = True
                elif j == 0:
                    i += 1
                    upDirection = True

        return res
