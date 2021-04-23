#!/usr/bin/python3
"""
Unlock all boxes
"""


def canUnlockAll(boxes):
    """
    All the boxes can be opened
    """
    ar = [0]
    if (len(boxes) == 0):
        return True
    for i in ar:
        for j in boxes[i]:
            if j not in ar:
                if j < len(boxes):
                    ar.append(j)
    if len(ar) == len(boxes):
        return True
    return False
