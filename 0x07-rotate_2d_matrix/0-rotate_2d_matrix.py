#!/usr/bin/python3
"""This module contains a function
"""


def rotate_2d_matrix(matrix):
    """This function rotates a 2D-Matrix
    """
    le, r = 0, len(matrix) - 1

    while le < r:
        for i in range(r - le):
            top, bottom = le, r

            topLeft = matrix[top][le + i]
            matrix[top][le + i] = matrix[bottom - i][le]
            matrix[bottom - i][le] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = topLeft
        r -= 1
        le += 1
