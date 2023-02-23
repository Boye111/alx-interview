#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """ determine the fewest number of coins needed to meet a given amount """
    if total <= 0:
        return 0

    else:
        m = sorted(coins)
        m.reverse()
        counter = 0
        for i in m:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
