from typing import List


def reverse_string(s: List[str]) -> None:
    """Reverse String

    Write a function that reverses a string. The input string is given as an
    array of characters char[].

    Do not allocate extra space for another array, you must do this by modifying
    the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.
    """
    s.reverse()


def reverse_integer(x: int) -> int:
    """ Reverse Integer

    Given a 32-bit signed integer, reverse digits of an integer.

    Note:
        Assume we are dealing with an environment which could only store
        integers within the 32-bit signed integer range: [−231,  231 − 1]. For
        the purpose of this problem, assume that your function returns 0 when
        the reversed integer overflows.
    """

    sign = 1
    if x < 0:
        x *= -1
        sign = -1

    n = 0
    while x > 0:
        n = n * 10
        n += x % 10
        x = x // 10

    res = sign*n
    if res < 0 and res < -2147483648:
        return 0
    if res > 0 and res > 2147483647:
        return 0

    return res


def first_unique_char(s: str) -> int:
    """First Unique Character in a String

    Given a string, find the first non-repeating character in it and return it's
    index. If it doesn't exist, return -1.

    Note:
        You may assume the string contain only lowercase letters.
    """
    unique = {}
    for c in s:
        if c not in unique:
            unique[c] = True
        else:
            unique[c] = False

    for idx, ch in enumerate(s):
        if unique[ch]:
            return idx

    return -1
