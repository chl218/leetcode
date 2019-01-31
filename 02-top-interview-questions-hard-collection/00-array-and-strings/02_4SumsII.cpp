class Solution {
   public:
      int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
         unordered_map<int,int> sums;
         for(int a : A) {
            for(int b : B) {
               sums[a+b]++;
            }
         }
         int zeroSums = 0;
         for(int c : C) {
            for(int d : D) {
               zeroSums += sums[-(c + d)];
            }
         }

         return zeroSums;
      }
};
