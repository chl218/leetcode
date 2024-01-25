"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true


Constraints:

   - 1 <= arr.length <= 104
   - 0 <= arr[i] <= 104

"""

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        mmax = max(arr)

        if arr[0] == mmax or arr[-1] == mmax:
            return False

        check_up = True
        curr = arr[0]
        for num in arr[1:]:

            if curr == mmax:
                check_up = False

            if check_up:
                if curr >= num:
                    return False
            elif curr <= num:
                return False

            curr = num

        return True


class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
