#!/usr/bin/python3
"""
This module has a function that determines
the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed
    to meet a given amount total
    """
    amounts = [total + 1] * (total + 1)
    amounts[0] = 0

    for coin in coins:
        for t in range(coin, total + 1):
            amounts[t] = min(amounts[t], amounts[t - coin] + 1)

    return -1 if amounts[total] == total +1 else amounts[total]
