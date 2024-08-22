#!/usr/bin/python3
"""
Module to determine the feest number coins needed to make change
"""

from typing import List


def count_coins(coins, total):
    # print(f"The coins for this round: {coins}")
    if not coins or (total == 0):
        if total > 0:
            return -1
        return 0
    coin = coins[0]
    coin_value = int(total / coin)
    balance = total % coin
    # print(f"{coin} gives {coin_value} coins, to balance {balance}")

    check_next = count_coins(coins[1:], balance)
    if check_next != -1:
        return coin_value + check_next

    return check_next


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
    split_coins = coins[:]
    for x in range(len(coins)):
        count = count_coins(split_coins, total)
        if count > 0:
            break
        # print("Starting over ----\n\n")
        split_coins = coins[:]
        del split_coins[(len(coins) - x - 2)]
        # print(f"New coins: {split_coins}")

    return int(count)


# print(makeChange([2, 3, 5, 6, 9], 100))
# print(makeChange([1, 2, 25], 100))
# print(makeChange([1, 2, 25], 37))
# print(makeChange([1256, 54, 48, 16, 102], 1453))
