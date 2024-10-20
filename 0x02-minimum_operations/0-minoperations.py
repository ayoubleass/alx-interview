#!/usr/bin/python3
"""
This module has a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
"""
import math


def minOperations(n):
    """
    calculates the fewest number
    of operations needed to result in exactly n H characters in the file.
    """
    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i
    return operations if n == 1 else 0
