#!/usr/bin/python3
"""Module to solve the n queens puzzle"""

import sys


def nqueens(n):
    """Function to place n non attacking queens on an NxN chessboard"""

    pass


if __name__ == "__main__":
    # Retrieve the passed values
    name = sys.argv[0]
    count = len(sys.argv)

    # If the wrong number of values is passed, abort
    if count != 2:
        print(f"Usage: nqueens N")
        sys.exit(1)

    # Retrieve N and confirm it to be an int
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
