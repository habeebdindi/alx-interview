#!/usr/bin/python3
"""This module contains various functions"""
from sympy import factorint


def minOperations(n):
    """calculates the fewest number of operations needed to result in exactly
    n H characters in the file."""
    prime_factors = factorint(n)
    return sum(k * v for k, v in prime_factors.items())
