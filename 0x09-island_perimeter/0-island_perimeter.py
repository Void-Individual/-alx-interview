#!/usr/bin/python3
"""Module to find the perimeter of a grid island"""


def island_perimeter(grid):
    """Function to return the perimeter of the island described in grid
    which is a list of list of integers"""

    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])

    for row in range(rows):
        for column in range(columns):
            # Check if the cell is a land square
            if grid[row][column] == 1:
                if (row == 0 or grid[row - 1][column] == 0):
                    perimeter += 1
                if (row == rows - 1 or grid[row + 1][column] == 0):
                    perimeter += 1

                if (column == 0 or grid[row][column - 1] == 0):
                    perimeter += 1

                if (column == columns - 1 or grid[row][column + 1] == 0):
                    perimeter += 1

    return perimeter
