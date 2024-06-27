#!/usr/bin/python3
"""Module replicating pascals triangle"""


def pascal_triangle(n):
    """Function to return a list of lists of integers
    representing a Pascal's triangle of n
    """

    if n <= 0:
        return []

    triangle = []
    last_row = []

    for row in range(n):
        current_row = []
        if row == 0:
            current_row = [1]
            last_row = current_row
        else:
            for count in range(row+1):
                if count == 0:
                    x = 0
                    y = last_row[0]
                else:
                    x = last_row[count - 1]
                    if count == len(last_row):
                        y = 0
                    else:
                        y = last_row[count]
                data = x + y
                current_row.append(data)
        triangle.append(current_row)
        last_row = current_row

    return triangle
