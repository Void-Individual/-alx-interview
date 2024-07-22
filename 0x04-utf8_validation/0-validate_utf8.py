#!/usr/bin/python3
"""Module containing a UTF-8 validator"""


def validUTF8(data):
    """Function to determine if data is a valid utf-8 recording"""

    for num in data:
        if num >= 128 or num < -128:
            return False
    return True
