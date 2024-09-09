#!/usr/bin/python3
"""Module containing a primegame function"""


def set_round_numbers(n):
    return list(range(1, n + 1))


def remove_factors(sel, round_numbers):
    next_round = []
    for num in round_numbers:
        if num % sel != 0:
            next_round.append(num)

    return next_round


def isWinner(x, nums):
    """Function to handle rounds of a prime game between 2 players
    Args:
        x - The number of rounds to be played
        nums - An array of n numbers to be used in each round

    Return:
        The name of the player that won the most rounds
        """

    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    # Monitor the points of each player
    player = {"Maria": 0, 'Ben': 0}
    # Set a check foreach player
    check_player = 0

    # Iterate over the passed no of rounds in the game
    for n in range(0, x):
        # Create a list of numbers for this round
        round_numbers = set_round_numbers(nums[n])
        # print(f"This rounds numbers: {round_numbers}")

        # Start the round
        while (round_numbers):
            # If there is only one option left in the game, end it
            if len(round_numbers) == 1:
                break

            next_no = round_numbers[1]
            # print(f"The next number is: {next_no}, player {check_player}")
            # Remove all the factors of the next number
            round_numbers = remove_factors(next_no, round_numbers)
            # print(f"After removal: {round_numbers}")

            # Move to the next player
            if check_player == 0:
                check_player = 1
            else:
                check_player = 0

        # Check the winner of the last round and score them
        if check_player == 0:
            player['Maria'] += 1
            # print("Maria wins this round")
        else:
            player['Ben'] += 1
            # print("Ben wins this round")

    # If Maria and ben have equal poins, then there is no winner
    if player['Maria'] == player['Ben']:
        return None
    # Else return the player with the most points
    return 'Maria' if player['Maria'] > player['Ben'] else 'Ben'


#    # Iterate over the passed no of rounds in the game
#    for n in range(0, x):
#        # Create a list of numbers for this round
#        round_numbers = set_round_numbers(nums[n])

#        # Start the round
#        print(f"This rounds numbers: {round_numbers}")
#        if (len(round_numbers) < 2):
#            if check_player == 0:
#                check_player = 1
#            else:
#                check_player = 0
#        else:
#            while (len(round_numbers) > 1):
#                # Move to the next player
#                if check_player == 0:
#                    check_player = 1
#                else:
#                    check_player = 0

#                next_player = round_numbers[1]
#            print(f"The next number is: {next_player}, player {check_player}")
#                # Remove all the factors of the next number
#                round_numbers = remove_factors(next, round_numbers)
#                print(f"After removal: {round_numbers}")

#        # Check the winner of the last round and score them
#        if check_player == 0:
#            player['Maria'] += 1
#        else:
#            player['Ben'] += 1

# print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
