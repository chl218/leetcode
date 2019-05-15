/**

Given a non-negative integer numRows, generate the first numRows of Pascal's
triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above
it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

**/

/**
 * Return an array of arrays.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** generate(int numRows, int** columnSizes) {

    *columnSizes = (int*)malloc(sizeof(int) * numRows);    
    int **ptri = (int**)malloc(sizeof(int*) * numRows);
    
    for(int row = 1; row <= numRows; row++) {    
        int *nums = (int*)malloc(sizeof(int)*row);
        nums[0] = 1;
        
        if(row == 1) {
            nums[0] = 1;
        }
        else if(row == 2) {
            nums[0] = 1;
            nums[1] = 1;
        }
        else {
            if(row % 2 == 0) {
                for(int j = 1; j < row/2; j++) {
                    nums[j] = ptri[row-2][j-1] + ptri[row-2][j];            
                }
                for(int ii = row/2 - 1, jj = row/2; jj < row; ii--, jj++) {
                    nums[jj] = nums[ii];
                }
            }
            else {                
                for(int j = 1; j <= row/2; j++) {
                    nums[j] = ptri[row-2][j-1] + ptri[row-2][j];
                }
                
                for(int ii = row/2 - 1, jj = row/2 + 1; jj < row; ii--, jj++) {
                    nums[jj] = nums[ii];
                }
            }
        }
        
        ptri[row-1] = nums;
    
        (*columnSizes)[row-1] = row;
        
    }

    return ptri;
}