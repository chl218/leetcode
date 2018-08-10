/**

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a
non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only
the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.


**/


// f(x) = x^2 - n
double f(double x, double n) {
    return x*x - n;
}

// f'(x) = 2x
double fprime(double x) {
    return 2*x;
}

/**
 * Newton's Method:
 * 
 * x_i = x_i-1 - f(x_i-1)/f'(x_i-1);
 *    where x_0 is initial guess
 *    and f(x) = x^2 - n
 *
 **/
int mySqrt(int x) {

    double x_curr;
    double x_prev = x>>1 == 0 ? 1 : x>>1; // initial guess
    for(int i = 0; i < 10000; i++) {
        x_curr = x_prev - f(x_prev, x)/fprime(x_prev);
        
        if((int)x_curr == (int)x_prev) {
            return x_curr;
        }
        
        x_prev = x_curr;
    }
    return x_curr;
}