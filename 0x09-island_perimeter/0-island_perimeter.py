#!/usr/bin/python3
"""Module to find the perimeter of a grid island"""


def island_perimeter(grid):
    """Function to return the perimeter of the island described in grid
    which is a list of list of integers"""

    perimeter = 0

    # Set a range restriction to avoid the top and bottom waters
    for row in range(1, len(grid) - 1):
        # Set range to avoid leftmost and rightmost waters
        for column in range(1, len(grid[row]) - 1):
            # Check if the cell is a land square
            if grid[row][column] == 1:
                if grid[row - 1][column] == 0:
                    perimeter += 1

                if grid[row + 1][column] == 0:
                    perimeter += 1

                if grid[row][column - 1] == 0:
                    perimeter += 1

                if grid[row][column + 1] == 0:
                    perimeter += 1

    return perimeter
