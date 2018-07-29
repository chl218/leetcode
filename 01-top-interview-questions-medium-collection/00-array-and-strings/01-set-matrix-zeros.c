/**

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do
it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

**/

void setZeroes(int** matrix, int matrixRowSize, int matrixColSize) {

    
    int cflag = 0;
    int rflag = 0;
    for(int c = 0; c < matrixColSize; c++) {
        if(matrix[0][c] == 0) {
            cflag = 1;
            break;
        }
    }
    for(int r = 0; r < matrixRowSize; r++) {
        if(matrix[r][0] == 0) {
            rflag = 1;
            break;
        }
    }
    
    
    for(int r = 1; r < matrixRowSize; r++) {
        for(int c = 1; c < matrixColSize; c++) {
            if(matrix[r][c] == 0) {
                matrix[r][0] = 0;
                matrix[0][c] = 0;
            }        
        }
    }
    
    for(int r = 1; r < matrixRowSize; r++) {
        if(matrix[r][0] == 0) {
            for(int c = 0; c < matrixColSize; c++) {
                matrix[r][c] = 0;
            }
        }
    }
    
    for(int c = 0; c < matrixColSize; c++) {
        if(matrix[0][c] == 0) {
            for(int r = 0; r < matrixRowSize; r++) {
                matrix[r][c] = 0;
            }
        }
    }
    
    if(cflag) {
        for(int c = 0; c < matrixColSize; c++) {
            matrix[0][c] = 0;
        }
    }
    if(rflag) {
        for(int r = 0; r < matrixRowSize; r++) {
            matrix[r][0] = 0;
        }
    }
    
}