class Solution:
    def tribonacci(self, n: int) -> int:
        """ Dynamic Tribonacci Number

        The Tribonacci sequence Tn is defined as follows:
        T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

        Given n, return the value of Tn.
        """

        T = [0, 1, 1]
        if n < 3:
            return T[n]

        soln = None
        for i in range(3, n+1):
            soln = T[0] + T[1] + T[2]
            T[0], T[1], T[2] = T[1], T[2], soln

        return soln
