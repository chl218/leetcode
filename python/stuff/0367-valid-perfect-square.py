"""
Given a positive integer num, write a function which returns True if num is a
perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.


Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false


Constraints:
    1 <= num <= 2^31 - 1

"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        i = 1
        while i * i <= num:
            if i * i == num:
                return True
            i += 1

        return False