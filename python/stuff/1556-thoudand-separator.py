"""
Given an integer n, add a dot (".") as the thousands separator and return it
in string format.


Example 1:
Input: n = 987
Output: "987"


Example 2:
Input: n = 1234
Output: "1.234"


Constraints:
    0 <= n <= 2^31 - 1

"""

class Solution:
    def thousandSeparator(self, n: int) -> str:

        nstr = str(n)

        tmp = []
        for i in range(len(nstr), 0, -3):

            if i-3 < 0:
                tmp.append(nstr[0:i])
            else:
                tmp.append(nstr[i-3:i])

        res = ''
        while tmp:
            res = res + tmp.pop() + '.'

        return res[:-1]

