#!/usr/bin/python3
""" This module contains a function"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []
    outer = []
    for i in range(n):
        inner = [1]
        if i == 0:
            outer.append(inner)
        else:
            if i > 1:
                for j in range(len(outer[i - 1]) - 1):
                    x = outer[i - 1][j] + outer[i - 1][j + 1]
                    inner.append(x)
                    j = j + 1
            inner.append(1)
            outer.append(inner)
        i = i + 1
    return outer
