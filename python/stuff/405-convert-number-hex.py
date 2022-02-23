
"""
Given an integer num, return a string representing its hexadecimal
representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there
should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve
this problem.


Example 1:
Input: num = 26
Output: "1a"


Example 2:
Input: num = -1
Output: "ffffffff"


Constraints:
    -2^31 <= num <= 2^31 - 1

"""

class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return  '0'

        hexmap = {
            "0000" : "0",
            "0001" : "1",
            "0010" : "2",
            "0011" : "3",
            "0100" : "4",
            "0101" : "5",
            "0110" : "6",
            "0111" : "7",
            "1000" : "8",
            "1001" : "9",
            "1010" : "a",
            "1011" : "b",
            "1100" : "c",
            "1101" : "d",
            "1110" : "e",
            "1111" : "f"
        }

        res = []
        for i in range(0, 32, 4):
            s = ""
            for j in range(i, i+4):
                s = str(num >> j & 1) + s

            res.append(hexmap[s])

        print(res)

        while res[-1] == '0':
            res.pop()

        res.reverse()
        return ''.join(res)



# def toHex(self, num):
#     if num==0: return '0'
#     mp = '0123456789abcdef'  # like a map
#     ans = ''
#     for i in range(8):
#         n = num & 15       # this means num & 1111b
#         c = mp[n]          # get the hex char
#         ans = c + ans
#         num = num >> 4
#     return ans.lstrip('0')  #strip leading zeroes