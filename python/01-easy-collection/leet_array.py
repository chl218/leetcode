from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """Remove Duplicates from Sorted Array

    Given a sorted array nums, remove the duplicates in-place such that each
    element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this by modifying
    the input array in-place with O(1) extra memory.

    :param
        Sorted array with duplicates
    :return
        New length of sorted array

    """
    if not nums:
        return 0

    curr = 1
    for i in range(1, len(nums)):
        if nums[curr-1] != nums[i]:
            nums[curr] = nums[i]    # note: no swapping
            curr += 1

    return curr
