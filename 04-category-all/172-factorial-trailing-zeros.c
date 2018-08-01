/**

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.

**/

/**
Ok, let’s look at how trailing zeros are formed in the first place. A trailing 
zero is formed when a multiple of 5 is multiplied with a multiple of 2. Now all 
we have to do is count the number of 5’s and 2’s in the multiplication.

Let’s count the 5’s first. 5, 10, 15, 20, 25 and so on making a total of 20. 
However there is more to this. Since 25, 50, 75 and 100 have two 5’s in each of 
them (25 = 5 * 5, 50 = 2 * 5 * 5, …), you have to count them twice. This makes 
the grand total 24. For people who like to look at it from a formula point of 
view

Number of 5’s = 100/5 + 100/25 + 100/125 + … = 24 (Integer values only)

Moving on to count the number of 2’s. 2, 4, 6, 8, 10 and so on. Total of 50 
multiples of 2’s, 25 multiples of 4’s (count these once more), 12 multiples of 
8’s (count these once more) and so on… The grand total comes out to

Number of 2’s = 100/2 + 100/4 + 100/8 + 100/16 + 100/32 + 100/64 + 100/128 + … 
= 97 (Integer values only)

Each pair of 2 and 5 will cause a trailing zero. Since we have only 24 5’s, we 
can only make 24 pairs of 2’s and 5’s thus the number of trailing zeros in 100 
factorial is 24.

**/


int trailingZeroes(int n) {
    
    int res = 0;

    while(n >= 5) {
        res += n / 5;
        n = n/5;
    }
    
    return res;
}