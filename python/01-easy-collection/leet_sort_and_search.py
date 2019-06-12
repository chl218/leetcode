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

    while end >= 0 and m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[end] = nums1[m]
            m -= 1
        else:
            nums1[end] = nums2[n]
            n -= 1
        end -= 1

    while n >= 0:
        nums1[end] = nums2[n]
        end -= 1
        n -= 1


def firstBadVersion(n):
    """First Bad Version

    You are a product manager and currently leading a team to develop a new
    product. Unfortunately, the latest version of your product fails the quality
    check. Since each version is developed based on the previous version, all
    the versions after a bad version are also bad.

    Suppose you have n versions [1, 2, ..., n] and you want to find out the
    first bad one, which causes all the following ones to be bad.

    You are given an API bool isBadVersion(version) which will return whether
    version is bad. Implement a function to find the first bad version. You
    should minimize the number of calls to the API.
    """

    def isBadVersion(version):
        v = 5
        return True if version == v else False

    b = 0
    e = n

    m = n // 2

    bad = n

    while e - b != 1:
        if isBadVersion(m):
            bad = m
            e = m
        else:
            b = m

        m = b + (e-b)//2

    return bad

