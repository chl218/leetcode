from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """Merge Sorted Array

    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
    one sorted array.

    Note:
        - The number of elements initialized in nums1 and nums2 are m and n
            respectively.
        - You may assume that nums1 has enough space (size that is greater or
            equal to m + n) to hold additional elements from nums2.

    Do not return anything, modify nums1 in-place instead.
    """
    end = m + n - 1

    m -= 1
    n -= 1

    while end >= 0 and m >=0 and n >=0:
        if nums1[m] > nums2[n]:
            nums1[end] = nums1[m]
            m -=1
        else:
            nums1[end] = nums2[n]
            n -= 1

        end -= 1


    while n >= 0:
        nums1[end] = nums2[n]
        end -= 1
        n -= 1

