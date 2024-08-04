#!/usr/bin/python3
"""Module to solve the n queens puzzle"""

import sys


def markTiles(n, tiles, queen):
    """Function to mark unpassable tiles"""

    # Horizontal
    x = queen[0]
    y = queen[1]

    horizontal = tiles[x]

    for a in range(n):
        tiles[a][y] = 1
        for tile in tiles:
            print(tile)
        print("Gap")
        # horizontal[a] = 1
        # print(horizontal)
        # print(tiles)
    # print(tiles)
    tiles[x] = horizontal
    # print(tiles)

    for _ in range(n):
        tiles[x][y] = 1

    # for tile in tiles:
    #    print(tile)


def nqueens(n):
    """Function to place n non attacking queens on an NxN chessboard"""

    tiles = [[0] * n] * n
    tiles[0][1] = 1
    for tile in tiles:
        print(tile)
    tiles = [[0] * n] * n

    queens = []
    for x in range(1):
        queen = []
        queen.append(x)
        queen.append(1)
        markTiles(n, tiles, queen)

        # for y in range(n):
        #    queen.append(y)
        # queens.append(queen)
    # print(queens)


if __name__ == "__main__":
    # Retrieve the passed values
    # name = sys.argv[0]
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
