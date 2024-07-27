#!/usr/bin/python3
"""Module containing a UTF-8 validator"""


def validUTF8(data):
    """Function to determine if given set of data is a valid utf-8 encoding"""

    number_bytes = 0

    # Most significant first bit of a byte
    MSB_1 = 1 << 7
    # Second most significant bit of a byte
    MSB_2 = 1 << 6

    for i in data:
        # Reset default MSB for this value
        mask_byte = 1 << 7

        # If this is not a continuation byte
        if number_bytes == 0:
            # Compare the most significant bits of the byte for
            # everytime it matches
            while mask_byte & i:
                """This loop will only activate if the value in binary
                is at least 10000000"""
                # Increment the number for the number of bytes
                number_bytes += 1
                # Bit shift to check the value of the next bit of the value
                mask_byte = mask_byte >> 1
                # This way, you wiil count the number of bits in i

            if number_bytes == 0:
                """This means the value is not a continuation byte,
                or part of a multibyte value"""
                continue
                # Move on to the next

            if number_bytes == 1 or number_bytes > 4:
                """If it is 1, it means its an invalid continuation byte that
                should not be placed here. If greater than 4, then it has gone
                beyond the 4-byte encoding system of utf8 and is invalid"""
                return False

        else:
            """This byte is supposed to be the continuation byte of a
            multi-byte value..."""
            if not (i & MSB_1 and not (i & MSB_2)):
                """Check if the first significant bit is 1, followed by 0,
                if not, its invalid"""
                return False
        """If there are more than 1 bytes, decrement before looping again.
        If its the end of a continuation byte,
        decrement to 0 to start counting again"""
        number_bytes -= 1

    """AT the end of the for loop, if there was no byte unaccounted for,
    the dataset passes"""
    if number_bytes == 0:
        return True
    # Then a byte has been left trailing with no follow-up
    return False
