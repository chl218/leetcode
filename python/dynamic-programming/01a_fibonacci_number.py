class Solution:
    def fib(self, n: int) -> int:
        """ Dynamic Fibonacci Sequence

        The Fibonacci numbers, commonly denoted F(n) form a sequence, called
        the Fibonacci sequence, such that each number is the sum of the two
        preceding ones, starting from 0 and 1. That is,

        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2), for n > 1.
        """
        f = [0, 1]

        if n < 2:
            return f[n]

        sln = None
        for i in range(2, n+1):
            sln = f[0] + f[1]
            f[0], f[1] = f[1], sln

        return sln
