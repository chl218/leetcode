"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r = len(grid)
        c = len(grid[0])

        islands = 0

        for m in range(len(grid)):
            for n in range(len(grid[0])):

                bfs = []

                if grid[m][n] == '1':
                    islands += 1
                    bfs.append((m, n))

                while bfs:
                    i, j = bfs.pop()
                    grid[i][j] = '0'
                    if i-1 >= 0 and grid[i-1][j] == '1':
                        bfs.append((i-1, j))
                    if i+1 < r and grid[i+1][j] == '1':
                        bfs.append((i+1, j))
                    if j-1 >= 0 and grid[i][j-1] == '1':
                        bfs.append((i, j-1))
                    if j+1 < c and grid[i][j+1] == '1':
                        bfs.append((i, j+1))

        return islands