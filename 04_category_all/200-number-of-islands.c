/**
Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

**/


void dfs(char **grid, int rowsz, int colsz, int x, int y) {
    
    grid[x][y] = '-';
    
    if(x-1 >= 0    && grid[x-1][y] == '1') dfs(grid, rowsz, colsz, x-1, y);
    if(x+1 < rowsz && grid[x+1][y] == '1') dfs(grid, rowsz, colsz, x+1, y);
    
    if(y-1 >= 0    && grid[x][y-1] == '1') dfs(grid, rowsz, colsz, x, y-1);
    if(y+1 < colsz && grid[x][y+1] == '1') dfs(grid, rowsz, colsz, x, y+1);
}


int numIslands(char** grid, int gridRowSize, int gridColSize) {
    int count = 0;
    
    for(int i = 0; i < gridRowSize; i++) {
        for(int j = 0; j < gridColSize; j++) {
            if(grid[i][j] == '1') {
                // printf("%d %d\n", i, j);
                dfs(grid, gridRowSize, gridColSize, i, j);
                count++;
            }
        }
    }
    
    return count;
}