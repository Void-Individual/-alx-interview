#!/usr/bin/python3
"""
Module to determine the feest number coins needed to make change
"""

from typing import List


def count_coins(coins, total):
    if (coins is None) or (total == 0):
        return 0
    coin = coins[0]
    # print(f"{coin} gives {(total / coin)}")
    count = int(total / coin) + count_coins(coins[1:], total % coin)
    return count


def makeChange(coins: List[int], total: int) -> int:
    """Function to determine the fewest number of passed coins needed to
    meet a given amount total

    args:
        coins - A list of values of coins in your possession
        total - The amount to reach

    Return:
        - If total is < 1, return 0
        - If total cannot be met by any number of coins, return -1
        - Otherwise, return the total number of coins
    """

    count = 0
    if total < 1:
        return count
    coins.sort(reverse=True)

    count = count_coins(coins, total)

    return int(count)


# print(makeChange([1, 2, 3, 5, 6, 4], 100))
# print(makeChange([1, 2, 25], 100))
# print(makeChange([1, 2, 25], 37))
# print(makeChange([1256, 54, 48, 16, 102], 1453))
