#include <vector>
using std::vector;

class Solution {
public:

    bool isPrime(int n) {
        for(int i = 2; i <= sqrt(n); i++) {
            if(n % i == 0) {
                return false;
            }
        }
        return true;
    }

    bool primeSubOperation(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++) {
            int bound;
            if(i == 0) {
                bound = nums[0];
            }
            else {
                bound = nums[i] - nums[i-1];
            }

            if(bound <= 0) {
                return false;
            }

            int largestPrime = 0;
            for(int j = bound - 1; j >= 2; j--) {
                if(isPrime(j)) {
                    largestPrime = j;
                    break;
                }
            }

            nums[i] = nums[i] - largestPrime;
        }    

        return true;
    }
};