"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

   Each row must contain the digits 1-9 without repetition.
   Each column must contain the digits 1-9 without repetition.
   Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.


Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isUnique(r, c) -> bool:
            if board[r][c] == '.':
                return True
            if board[r][c] in unique:
                return False
            unique.add(board[r][c])
            return True

        blocks = [[0, 3, 0, 3], [0, 3, 3, 6], [0, 3, 6, 9],
                  [3, 6, 0, 3], [3, 6, 3, 6], [3, 6, 6, 9],
                  [6, 9, 0, 3], [6, 9, 3, 6], [6, 9, 6, 9]]

        for b in blocks:
            unique = set()
            for r in range(b[0], b[1]):
                for c in range(b[2], b[3]):
                    if not isUnique(r, c):
                        return False

        for c in range(0, 9):
            unique = set()
            for r in range(0, 9):
                if not isUnique(r, c):
                    return False

        for r in range(0, 9):
            unique = set()
            for c in range(0, 9):
                if not isUnique(r, c):
                    return False

        return True