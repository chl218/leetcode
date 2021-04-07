"""
You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y]
(i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed
that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements
of arr equal.



Example 1:

Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

Example 2:

Input: n = 6
Output: 9


Constraints:

    1 <= n <= 10^4
"""


class Solution:
    def minOperations(self, n: int) -> int:

        if n % 2 == 0:
            target = (2*(n//2)-1) + 1
        else:
            target = (2*(n//2)) + 1

        ops = 0
        for i in range(n//2):

            lhs = (2*i) + 1
            rhs = (2*(n-1-i)) + 1

            while lhs != target or rhs != target:
                if lhs == target and rhs != target:
                    ops += 1
                    rhs -= 1
                elif lhs != target and rhs == target:
                    ops += 1
                    lhs += 1
                else:
                    ops += 1
                    lhs += 1
                    rhs -= 1

        return ops


"""
The main thing in this problem is that we must realize that to make array equal in minimum operations, we need to make
all the elements equal to the Mid element (which would be equal to n). Also, if we make the first half equal to the mid
element, the other half will also become equal since one operation consists of adding and subtracting. There will always
be a pair of elements which need same number of addition and subtraction to become equal to mid.

For this, there exists two cases. You may understand it better if you consider an example alongside -

    n is Odd : In this case, all the elements need to become equal to the mid element( equal to n). This is done by
    adding 1 to elements smaller than mid and subtracting 1 from elements bigger than mid till all become equal.

    The total number of operations needed are - 2 + 4 + 6 + 8 + ... (n - 1) /2 elements. How (n - 1) / 2 elements ?
    These correspond to the number to elements coming before mid. So, we need to apply operations to all those elements
    (2 times, 4 times, 6 times and so on...).

    The given equation is in Arithmetic Progression, which can be simplified to -

    => N * [a + ((N - 1) * d) / 2]      // A.P Formula
    =  N * [2 + ((N -1)) * 2) / 2]
    =  N * [2 + N - 1]
    =  N * [N + 1]
    where N = number of elements in the Arithmetic Progression = (n -1) / 2

    n is Even - In this case, all the elements need to become equal to the mean of mid elements (equal to n). Again,
    the operations are applied as in the case when n is odd by adding to smaller than mid & subtracting from larger
    than mid elements.

    The total number of operations needed are - 1 + 3 + 5 + 7 + ... n /2 elements. How n / 2 elements ? These again
    correspond to the number to elements coming before the mean of mid elements. In even case, the first half and
    second half contains n/2 elements each. So, we need to apply operations to all those elements (1 times, 3 times,
    5 times and so on...).

    The given equation is in Arithmetic Progression, which can be simplified to -

    => N * [a + ((N - 1) * d) / 2]      // A.P Formula
    =  N * [1 + ((N - 1) * 2) / 2]
    =  N * [1 + N - 1]
    =  N * N
    where N = number of elements in the Arithmetic Progression = n / 2
"""
def minOperations(self, n: int) -> int:
   if n % 2 != 0:
      N = (n-1)//2
      return N * (N+1)

   N = n // 2
   return N * N