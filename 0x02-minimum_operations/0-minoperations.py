#!/usr/bin/python3
"""This module contains various functions"""


def get_factors(n):
    """This function returns the factors of a number"""
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            complement = n // i
            if complement != i:  # Avoid adding the square root twice
                factors.append(complement)
    return factors


def minOperations(n):
    """Calculates the fewest number of operations needed to result in exactly
    n H characters in the file."""
    if n < 2:
        return 0

    factors = get_factors(n)
    prime_factors = [factor for factor in factors if len(
        get_factors(factor)) < 3]

    p_factor_occurrence = {}
    for factor in prime_factors[1:]:
        count = 0
        while n % factor == 0:
            n //= factor
            count += 1
        if count > 0:
            p_factor_occurrence[factor] = count

    minOps = 0
    for k, v in p_factor_occurrence.items():
        minOps += k * v

    return minOps
