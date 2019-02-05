/**

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3]
must equally likely to be returned.

solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

**/

class Solution {
    
private:
    vector<int> copy;
    vector<int> to_shuffle;
    
public:
    Solution(vector<int> nums) {
        std::vector<int>::iterator b = nums.begin();
        std::vector<int>::iterator e = nums.end();
        while(b != e) {
            copy.push_back(*b);
            to_shuffle.push_back(*b);
            b++;
        }
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return copy;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        std::random_shuffle(to_shuffle.begin(), to_shuffle.end());
        return to_shuffle;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */