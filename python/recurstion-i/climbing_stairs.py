"""
You are climbing a staircase. It takes n steps to reach the top. Each time you
can either climb 1 or 2 steps. In how many distinct ways can you climb to the
top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:
    1 <= n <= 45

Hide Hint #1
   To reach nth step, what could have been your previous steps? (Think about
      the step sizes)
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}

        def aux(N):
            if N in cache:
                return cache[N]

            if N == 1:
                return 1
            if N == 2:
                return 2

            cache[N] = aux(N-1) + aux(N-2)
            return cache[N]

        return aux(n)
