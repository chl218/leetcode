/**

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

**/

void rotate(int** matrix, int matrixRowSize, int *matrixColSizes) {
    
    int N = matrixRowSize;
    // transpose
    for(int r = 0; r < N; r++) {
        for(int c = r; c < N; c++){
            if(r == c) continue;
            
            int tmp = matrix[r][c];
            matrix[r][c] = matrix[c][r];
            matrix[c][r] = tmp;
        }
    }
    
    
    // flip col
    for(int r = 0; r < N; r++) {
        int b = 0, e = N-1;
        while(b < e) {
            int tmp = matrix[r][b];
            matrix[r][b] = matrix[r][e];
            matrix[r][e] = tmp;
            b++;
            e--;
        }
    }

}
