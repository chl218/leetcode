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


def single_umber(nums: List[int]) -> int:
    """Single Number

    Given a non-empty array of integers, every element appears twice except for
     one. Find that single one.

    Note: Your algorithm should have a linear runtime complexity. Could you
    implement it without using extra memory?
    """

    # n xor 0 = n
    # n xor n = 0

    unique = 0
    for n in nums:
        unique ^= n

    return unique


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """Intersection of Two Arrays II

    Given two arrays, write a function to compute their intersection.

    Note:
        - Each element in the result should appear as many times as it shows in
          both arrays.
        - The result can be in any order.
    """

    nums1.sort()
    nums2.sort()

    res = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            res.append((nums1[i]))
        elif nums1[i] > nums2[j]:
            j += 1
        else:   # nums1[i] < nums2[j]:
            i += 1

    return res


def plus_one(digits: List[int]) -> List[int]:
    """Plus One

    Given a non-empty array of digits representing a non-negative integer, plus
    one to the integer.

    The digits are stored such that the most significant digit is at the head of
     the list, and each element in the array contain a single digit.

    You may assume the integer does not contain any leading zero, except the
    number 0 itself.
    """

    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        sum = digits[i] + carry
        carry = sum // 10   # // - integer division
        digits[i] = sum % 10

    if carry > 0:
        digits = [carry] + digits

    return digits


def move_zeroes(nums: List[int]) -> None:
    """Move Zeros

    Given an array nums, write a function to move all 0's to the end of it
    while maintaining the relative order of the non-zero elements.

    Do not return anything, modify nums in-place instead.
    """

    num_zeros = 0

    i = 0
    for n in nums:
        if n != 0:
            nums[i] = n
            i += 1
        else:
            num_zeros += 1

    nums[len(nums) - num_zeros:] = [0] * num_zeros


def two_sum(nums: List[int], target: int) -> List[int]:
    """Two Sum

    Given an array of integers, return indices of the two numbers such that they
    add up to a specific target.

    You may assume that each input would have exactly one solution, and you may
    not use the same element twice.
    """
    dict = {}

    for i in range(len(nums)):
        if (target - nums[i]) in dict:
            return [dict[target - nums[i]], i]
        else:
            dict[nums[i]] = i

