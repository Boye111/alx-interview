#!/usr/bin/python3
"""
alx interview questions
"""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for x in range(1, len(boxes) - 1):
        checked_boxes = False
        for idx in range(len(boxes)):
            checked_boxes = x in boxes[idx] and x != idx
            if checked_boxes:
                break
        if checked_boxes is False:
            return checked_boxes
    return True
