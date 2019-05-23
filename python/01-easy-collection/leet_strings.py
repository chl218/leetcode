from typing import List
from collections import Counter


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
        integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For
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

    res = sign * n
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


def is_anagram(s: str, t: str) -> bool:
    """Valid Anagram

    Given two strings s and t , write a function to determine if t is an anagram
    of s.

    Note:
        You may assume the string contains only lowercase alphabets.

    Follow up:
        What if the inputs contain unicode characters? How would you adapt your
        solution to such case?
    """

    ##########
    # SLOW
    ##########
    # hash = {}
    # for ch in s:
    #     if ch not in hash:
    #         hash[ch] = 1
    #     else:
    #         hash[ch] += 1
    #
    # for ch in t:
    #     if ch not in hash or hash[ch] == 0:
    #         return False
    #     else:
    #         hash[ch] -= 1
    #
    # return sum(hash.values()) == 0

    if len(s) != len(t):
        return False

    s_dict = Counter(s)
    t_dict = Counter(t)

    for key in s_dict.keys():
        if key not in t_dict:
            return False

        if s_dict[key] != t_dict[key]:
            return False

    return True


def is_palindrome(s: str) -> bool:
    """Valid Palindrome

    Given a string, determine if it is a palindrome, considering only
    alphanumeric characters and ignoring cases.

    Note:
        For the purpose of this problem, we define empty string as valid
        palindrome.
    """
    s = s.lower()

    i = 0
    j = len(s) - 1

    while i < j:

        if s[i] != s[j]:
            if s[i].isalnum() and s[j].isalnum():
                return False

            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -= 1
        else:
            i += 1
            j -= 1

    return True


def my_atoi(s: str) -> int:
    """String to Integer (atoi)

    Implement atoi which converts a string to an integer.

    The function first discards as many whitespace characters as necessary until
    the first non-whitespace character is found. Then, starting from this
    character, takes an optional initial plus or minus sign followed by as many
    numerical digits as possible, and interprets them as a numerical value.

    The string can contain additional characters after those that form the
    integral number, which are ignored and have no effect on the behavior of
    this function.

    If the first sequence of non-whitespace characters in str is not a valid
    integral number, or if no such sequence exists because either str is empty
    or it contains only whitespace characters, no conversion is performed.

    If no valid conversion could be performed, a zero value is returned.

    Note:
        Only the space character ' ' is considered as whitespace character.

        Assume we are dealing with an environment which could only store
        integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If
        the numerical value is out of the range of representable values,
        INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned

    """

    idx = 0
    while idx < len(s) and s[idx] == ' ':
        idx += 1

    if idx >= len(s):
        return 0

    sign = 1
    if s[idx] == '-':
        sign = -1
        idx += 1
    elif s[idx] == '+':
        idx += 1
    elif s[idx].isalpha():
        return 0

    n = 0
    for i in range(idx, len(s)):

        if not s[i].isdigit():
            return n

        n *= 10

        if sign < 0:
            n -= ord(s[i]) - ord('0')
            if n < -2147483648:
                return -2147483648
        else:
            n += ord(s[i]) - ord('0')
            if n > 2147483647:
                return 2147483647

    return n


def str_str(haystack: str, needle: str) -> int:
    """Implement strStr()

    Return the index of the first occurrence of needle in haystack, or -1 if
    needle is not part of haystack.

    For the purpose of this problem, we will return 0 when needle is an empty
    string. This is consistent to C's strstr() and Java's indexOf().
    """

    if haystack == needle:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1

