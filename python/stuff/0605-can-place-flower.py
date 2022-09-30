"""
You have a long flowerbed in which some of the plots are planted, and some are
not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty
and 1 means not empty, and an integer n, return if n new flowers can be planted
in the flowerbed without violating the no-adjacent-flowers rule.


Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true


Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:
    1 <= flowerbed.length <= 2 * 10^4
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length

"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        if len(flowerbed) == 1:
            if n == 1 and flowerbed[0] == 0:
                return True
            return False

        len_fb = len(flowerbed)
        for i in range(len_fb):

            if i-1 >= 0 and i+1 < len_fb:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif i-1 >= 0:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif i+1 < len_fb:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1

            if n == 0:
                return True

        return n == 0