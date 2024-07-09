#!/usr/bin/python3
"""Module containing a function for minimum operations"""

from typing import Tuple


def copy_all(count: int, file: str) -> Tuple[int, str]:
    """Function to copy the entire string content and increase
    count value by 1"""

    return count + 1, file


def paste(count: int, file: str, copy: str) -> Tuple[int, str]:
    """Function to concatenate the last copied content and
    increment the count value by 1"""

    return count + 1, file + copy


def check_factor(n: int, src: str) -> int:
    """Function to check if the current file length is a factor
    of the desired value"""

    if n % len(src):
        return 0
    return 1


def minOperations(n: int) -> int:
    """Function to determine the minimum number of operations required
    to rewrite a single letter"""

    file = 'H'
    count = 0
    copy = ''

    while (len(file) < n):
        factor = check_factor(n, file)

        if (factor) and (len(file + copy) <= n / 2):
            count, copy = copy_all(count, file)
        else:
            pass

        count, file = paste(count, file, copy)

    return count
