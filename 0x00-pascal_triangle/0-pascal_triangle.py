#!/usr/bin/python3
""" This module contains a function"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []
    outer = [[1]]
    for i in range(1, n):
        inner = [1]
        for j in range(1, i):
            x = outer[i - 1][j - 1] + outer[i - 1][j]
            inner.append(x)
        inner.append(1)
        outer.append(inner)
    return outer
