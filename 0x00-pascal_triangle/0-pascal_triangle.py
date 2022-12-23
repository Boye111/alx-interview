#!/usr/bin/python3
"""
Pascals Triangle interview
"""


def pascal_triangle(n):
    """ technical interview """
    for i in range(n+1):
        for j in range(n-1):
            print(' ', end='')

        x = 1
        for j in range(1, i+1):
            print (x, ' ', sep='', end='')
            x = x * (i - j) // j
        print()
