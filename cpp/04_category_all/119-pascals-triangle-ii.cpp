/**

Given a non-negative index k where k ≤ 33, return the kth index row of the
Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above
it.

Example:

Input: 3
Output: [1,3,3,1]

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

**/

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if(rowIndex < 1) {
            vector<int> res;
            for(int i = 0; i <= rowIndex; i++) {
                res.push_back(1);
            }
            return res;
        }
        
        list<int> res;
        
        res.push_back(1);
        res.push_back(1);
        
        int i = 2; 
        while(i <= rowIndex) {
            int size = res.size();
            
            res.push_back(1);
        
            int n1 = res.front(); res.pop_front(); size--;
            int n2;
            while(size) {
                n2 = res.front(); res.pop_front(); size--;
                res.push_back(n1 + n2);
                
                n1 = n2;
            }
            res.push_back(1);
            
            i++;
        }
        
        return vector<int>(res.begin(), res.end());
    }
};