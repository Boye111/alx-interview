#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """ method that determines if a data set represents a valid UTF-8 """
    byte = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:
        mask_byte = 1 << 7
        if byte == 0:
            while mask_byte & i:
                byte += 1
                mask_byte = mask_byte >> 1

            if byte == 0:
                continue

            if byte == 1 or byte > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False

        byte -= 1

    if byte == 0:
            return True

    return False
