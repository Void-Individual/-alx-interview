#!/usr/bin/python3
"""
Module to determine the feest number coins needed to make change
"""

from typing import List


def count_coins(coins, total):
    """A function to run recursively while checking the coin list as it
    reduces and comparing it to the total balance"""

    # print(f"The coins for this round: {coins}")

    # If the coin list is empty or The balance is 0
    if not coins or (total == 0):
        # If the coin list is empty but the balance is not 0, it fails
        if total > 0:
            return -1
        return 0

    coin = coins[0] # Select the coin for this iteration
    # The coin value from the total
    coin_value = int(total / coin)
    # The balance after you remove the coin value
    balance = total % coin
    # print(f"{coin} gives {coin_value} coins, to balance {balance}")

    # Recursively check the next coins on the list
    check_next = count_coins(coins[1:], balance)

    # If the recursion call doesn't fail, end with +ve no of coins
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

    # Arrange the coins in descending order
    coins.sort(reverse=True)

    # Make a copy of the wallet coins
    split_coins = coins[:]

    # Begin the iteration
    for x in range(len(coins)):
        # Check the number of coins with the current list of coins
        count = count_coins(split_coins, total)

        # If count is a positive number, it has passed
        if count > 0:
            break

        # print("Starting over ----\n\n")
        # Copy the otiginal coin list again due to mods
        split_coins = coins[:]

        # Delete the negative index by incremental values and run again
        del split_coins[(len(coins) - x - 2)]

        # print(f"New coins: {split_coins}")

    return int(count)


# print(makeChange([2, 3, 5, 6, 9], 100))
# print(makeChange([1, 2, 25], 100))
# print(makeChange([1, 2, 25], 37))
# print(makeChange([1256, 54, 48, 16, 102], 1453))
