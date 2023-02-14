"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.

"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:


        def add(a:str, b:str) -> str:

            res = ""
            cout = 0
            for i in range(len(a)-1, -1, -1):

                if a[i] == "0" and b[i] == "1" or \
                   a[i] == "1" and b[i] == "0":
                    if cout == 0:
                        res = "1" + res
                    else:
                        res = "0" + res
                elif a[i] == "1" and b[i] == "1":
                    if cout == 0:
                        res = "0" + res
                    else:
                        res = "1" + res
                    cout = 1
                else:
                    if cout == 0:
                        res = "0" + res
                    else:
                        res = "1" + res
                        cout = 0

            return ("1"*cout) + res


        if len(a) > len(b):
            return add(a, ("0"*(len(a)-len(b))) + b)

        if len(a) < len(b):
            return add(("0"*(len(b)-len(a))) + a, b)

        return add(a, b)