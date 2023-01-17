"""
54. Spiral Matrix

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
        spiral = []

        l_bound = 0
        r_bound = len(matrix) - 1

        t_bound = 0
        b_bound = len(matrix[0]) - 1

        direction = 1
        while l_bound <= r_bound and t_bound <= b_bound:

            if direction == 1:
                for i in range(l_bound, r_bound+1):
                    spiral.append(matrix[t_bound][i])
                t_bound += 1

            if direction == 2:
                for j in range(t_bound, b_bound+1):
                    spiral.append(matrix[j][r_bound])
                r_bound -= 1

            if direction == 3:
                for i in range(r_bound, l_bound-1, -1):
                    spiral.append(matrix[b_bound][i])
                b_bound -= 1

            if direction == 4:
                for j in range(b_bound, t_bound-1, -1):
                    spiral.append(matrix[j][l_bound])
                l_bound += 1

            direction = (direction % 4) + 1

        return spiral

