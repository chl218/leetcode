from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """Remove Duplicates from Sorted Array

    Given a sorted array nums, remove the duplicates in-place such that each
    element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this by modifying
    the input array in-place with O(1) extra memory.
    """

    if not nums:
        return 0

    curr = 1
    for i in range(1, len(nums)):
        if nums[curr-1] != nums[i]:
            nums[curr] = nums[i]    # note: no swapping
            curr += 1

    return curr


def max_profit(prices: List[int]) -> int:
    """Best Time to Buy and Sell Stock II

    Say you have an array for which the ith element is the price of a given
    stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many
    transactions as you like (i.e., buy one and sell one share of the stock
    multiple times).

    Note: You may not engage in multiple transactions at the same time (i.e.,
    you must sell the stock before you buy again).
    """

    # Peak-Vally Approach
    #   TotalProfit = sum_i(height(peak_i) - height(vally_i))
    profit = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            profit += prices[i+1] - prices[i]

    return profit


def rotate(nums: List[int], k: int) -> None:
    """Rotate Array

    Given an array, rotate the array to the right by k steps, where k is
    non-negative.

    Python slicing approach
    """

    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]     # nums[:] - modify in-place


def rotate2(nums: List[int], k: int) -> None:
    """Rotate Array

    Given an array, rotate the array to the right by k steps, where k is
    non-negative.

    Algorithm approach: Reversal Algorithm (right rotation):


        Let AB are the two parts of the input array where A = arr[0..d-1] and
        B = arr[d..n-1]. The idea of the algorithm is :

        Reverse A to get ArB, where Ar is reverse of A.
        Reverse B to get ArBr, where Br is reverse of B.
        Reverse all to get (ArBr) r = BA.
    """

    k = k % len(nums)
    nums.reverse()
    nums[:k+1] = nums[k::-1]
    nums[k:] = nums[:k:-1]


def contains_duplicate(nums: List[int]) -> bool:
    """Contains Duplicate

    Given an array of integers, find if the array contains any duplicates.

    Your function should return true if any value appears at least twice in the
    array, and it should return false if every element is distinct.
    """

    unique = set(nums)
    if len(nums) == len(unique):
        return False
    return True

