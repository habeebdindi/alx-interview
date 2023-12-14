#!/usr/bin/python3
"""This module contains various functions"""


def get_factors(n):
    """This function returns the factors of a number"""
    factors = [i for i in range(1, int(n) + 1) if n % i == 0]
    return factors


def even(n):
    """This function handles when the input to minOp func is even"""
    if n == 1:
        return ['C', 'P']
    operations = []
    if n % 2 == 0:
        operations += even(n // 2)
    else:
        if len(get_factors(n)) > 2:
            operations += odd(n)
        else:
            operations.append('C')
            operations += ['P' for i in range(int(n) - 1)]
    operations += ['C', 'P']
    return operations


def odd(n):
    """This function handles when the input to minOp func is even
    operations = ['C']
    factors = get_factors(n)
    operations += ['P' for i in range(0, factors[-2] - 1)]
    operations.append('C')
    operations += ['P' for i in range((int(n) // factors[-2]) - 1)]
    return operations
    """
    if n == 1:
        return ['C', 'P', 'P']
    operations = []
    if n % 3 == 0:
        operations += odd(n // 3)
    else:
        operations.append('C')
        operations += ['P' for i in range(int(n) - 1)]
    operations += ['C', 'P', 'P']
    return operations


def minOperations(n):
    """calculates the fewest number of operations needed to result in exactly
    n H characters in the file."""
    result = 0
    if n < 2:
        return result
    if n % 2 == 0:
        result = even(n / 2)
    else:
        factors = get_factors(n)
        if len(factors) > 2:
            result = odd(n / 3)
    if result:
        return len(result)
    return n
