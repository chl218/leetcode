/**

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4

Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

**/

int countPrimes(int n) {
    int count = 0;
    
    int *sieve = (int*)malloc(sizeof(int) * n);

    sieve[0] = 0;
    sieve[1] = 0;
    for(int i = 2; i < n; i++) {
        sieve[i] = 1;
    }
    
    
    int nsqrt = sqrt(n) + 1;
    for(int i = 2; i < nsqrt; i++) {
        
        if(sieve[i]) {
            for(int j = i<<1; j < n; j += i) {
                sieve[j] = 0;
            }
            // count++;
        }
        
    }
    
    for(int i = 0; i < n; i++) {
        count += sieve[i];

    }
    return count;
}