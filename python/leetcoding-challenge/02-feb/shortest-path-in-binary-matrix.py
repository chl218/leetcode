"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k
such that:

    Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
    C_1 is at location (0, 0) (ie. has value grid[0][0])
    C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
    If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).

Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist,
return -1.


Example 1:

Input: [[0,1],[1,0]]
Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4


Note:

   - 1 <= grid.length == grid[0].length <= 100
   - grid[r][c] is 0 or 1

"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROW = 0
        COL = 0

        queue = []
        paths = {}
        min_paths = []

        def bfs(path_len: int, r: int, c: int):
            if r >= 0 and r < ROW and c >= 0 and c < COL and grid[r][c] == 0:
                queue.append((r, c))
                paths[(r, c)] = path_len
                grid[r][c] = 1              # mark current coord visited

        if not grid or grid[0][0] != 0:
            return -1

        ROW = len(grid)
        COL = len(grid[0])

        queue = [(0, 0)]
        paths = {(0, 0): 1}

        while queue:
            r, c = queue.pop(0)

            if r == ROW - 1 and c == COL - 1:
                min_paths.append(paths[(r, c)])
            else:

                next_len = paths[(r, c)] + 1

                bfs(next_len, r+1, c)           # down
                bfs(next_len, r-1, c)           # up
                bfs(next_len, r, c+1)           # right
                bfs(next_len, r, c-1)           # left

                bfs(next_len, r-1, c-1)         # diag-up-left
                bfs(next_len, r-1, c+1)         # diag-up-right
                bfs(next_len, r+1, c-1)         # diag-down-left
                bfs(next_len, r+1, c+1)         # diag-down-right

        if not min_paths:
            return -1
        else:
            return min(min_paths)
