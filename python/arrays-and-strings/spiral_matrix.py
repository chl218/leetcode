"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100

"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])

        lb, rb = 0, n-1
        tb, bb = 1, m-1

        spiral = []

        heading, i, j = 'E', 0, 0
        for _ in range(m*n):

            spiral.append(matrix[i][j])

            if heading == 'N':
                if i > tb:
                    i -= 1
                else:
                    heading = 'E'
                    tb = i + 1
                    j += 1
            elif heading == 'S':
                if i < bb:
                    i += 1
                else:
                    heading = 'W'
                    bb = i - 1
                    j -= 1

            elif heading == 'E':
                if j < rb:
                    j += 1
                else:
                    heading = 'S'
                    rb = j - 1
                    i += 1
            elif heading == 'W':
                if j > lb:
                    j -= 1
                else:
                    heading = 'N'
                    lb = j + 1
                    i -= 1

        return spiral
