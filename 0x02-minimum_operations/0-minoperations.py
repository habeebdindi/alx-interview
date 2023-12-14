#!/usr/bin/python3
"""This module contains various functions"""


def get_factors(n):
    """This function returns the factors of a number"""
    return [i for i in range(1, int(n) + 1) if n % i == 0]


def get_prime_factors(factors):
    """Returns the prime factors in a list"""
    return [key for key in factors if len(get_factors(key)) < 3]


def no_of_times(n, div):
    """Retruns the number of times a number divides a number"""
    if n % div != 0:
        return 0
    return 1 + no_of_times(n / div, div)


def minOperations(n):
    """calculates the fewest number of operations needed to result in exactly
    n H characters in the file."""
    if n < 2:
        return 0
    factors = get_factors(n)
    prime_factors = get_prime_factors(factors)
    p_factor_occurence = {k: no_of_times(n, k) for k in prime_factors[1:]}
    minOps = 0
    for k, v in p_factor_occurence.items():
        minOps += k * v
    return minOps
