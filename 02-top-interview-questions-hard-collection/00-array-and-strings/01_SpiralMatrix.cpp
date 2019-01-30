class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if(matrix.size() == 0) {
            return vector<int>();
        }
        int left = 0, right = matrix[0].size()-1;
        int top = 0, bottom = matrix.size()-1;
                
        vector<int> spiral;
        
        const int TO_LEFT = 1, TO_BOTTOM = 2, TO_RIGHT = 3, TO_TOP = 4;
        
        int state = TO_LEFT;
        while(left <= right && top <= bottom) {
            
            int col = 0, row = 0;
            switch(state) {
                case TO_LEFT:
                    col = left;
                    while(col <= right){
                        spiral.push_back(matrix[top][col]);
                        col++;
                    }
                    top++;
                    state = TO_BOTTOM;
                    break;
                case TO_BOTTOM:
                    row = top;
                    while(row <= bottom) {
                        spiral.push_back(matrix[row][right]);
                        row++;
                    }
                    right--;
                    state = TO_RIGHT;
                    break;
                case TO_RIGHT:
                    col = right;
                    while(col >= left) {
                        spiral.push_back(matrix[bottom][col]);
                        col--;
                    }
                    bottom--;
                    state = TO_TOP;
                    break;
                case TO_TOP:
                    row = bottom;
                    while(row >= top) {
                        spiral.push_back(matrix[row][left]);
                        row--;
                    }
                    left++;
                    state = TO_LEFT;
                    break;
            }
        }
        
        return spiral;
    }
};
