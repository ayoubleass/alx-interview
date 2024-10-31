#!/usr/bin/python3
"""
This module has a function that
Checks if the given data is valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Checks if the given data is valid UTF-8 encoding.
    Returns:
        True if the data is valid UTF-8, False otherwise.
    """
    if not data:
        return False
    bytes_size = 0
    for byte in data:
        if bytes_size == 0:
            bits = 1 << 7
            while byte & bits:
                bytes_size += 1
                bits >>= 1
            if bytes_size == 1 or bytes_size > 4:
                return False
            if bytes_size == 0:
                return True
        else:
            if not (byte & 0xC0 == 0x80):
                return False
        bytes_size -= 1
    return bytes_size == 0
