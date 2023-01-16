#!/usr/bin/python3
"""
Alx minimum operations
"""


def minOperations(n):
    """ function that calculates the minimum operations to get to a given
    number of characters in the minimum operations """
    x = 1
    start = 0
    counter = 0
    while x < n:
        remainder = n - x
        if (remainder % x == 0):
            start = x
            x += start
            counter += 2
        else:
            x += start
            counter += 1

    return counter
