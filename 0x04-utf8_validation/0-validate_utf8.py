# !/usr/bin/python3
"""Module containing a UTF-8 validator"""


def validUTF8(data):
    """Function to determine if given set of data is a valid utf-8 encoding"""

    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    # bin_data = {}
    for i in data:
        # bin_data[i] = bin(i)[2:]
        mask_byte = 1 << 7

        if number_bytes == 0:
            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                # print(bin_data)
                return False

        number_bytes -= 1

    # print(bin_data)

    if number_bytes == 0:
        return True

    return False
