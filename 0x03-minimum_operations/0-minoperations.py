#!/usr/bin/python3

"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    minimum of operations
    """


    numOper = 0
    divN = n
    numTimes = 2

    if n <= 1:
        return 0
    while divN > 1:
        if (divN % numTimes) == 0:
            divN = divN / numTimes
            divN = round(divN)
            numOper += numTimes
        else:
            numTimes += 1
    return numOper