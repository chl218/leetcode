class Solution {
public:
    
    bool dfs(vector<vector<char>>& board, int M, int N, int x, int y, string& word, int idx) {
        if(idx == word.length()) {
            return true;
        }
        
        if(x < 0 || y < 0 || x >= M || y >= N || board[x][y] != word[idx]) {
            return false;
        }     
    
        idx++;
        
        board[x][y] = '*';    
        bool traverse = dfs(board, M, N, x-1, y, word, idx) ||
                        dfs(board, M, N, x+1, y, word, idx) ||
                        dfs(board, M, N, x, y-1, word, idx) ||
                        dfs(board, M, N, x, y+1, word, idx);
        board[x][y] = word[--idx];
        
        return traverse;
   }
    
    bool exist(vector<vector<char>>& board, string word) {
        if(word.empty()) {
            return true;
        }
        if(board.empty() || board[0].empty()) {
            return false;
        }
        
        int M = board.size();
        int N = board[0].size();
        for(int i = 0; i < M; i++) {
            for(int j = 0; j < N; j++) {
                if(dfs(board, M, N, i, j, word, 0)) {
                    return true;
                }
            }
        }
        
        return false;
    }
};