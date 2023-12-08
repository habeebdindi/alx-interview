#!/usr/bin/python3
"""This module contains a function"""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened"""

    [box.append('F') for box in boxes[1:]]
    boxes[0].append('T')

    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            for k in range(len(boxes)):
                if boxes[i][j] == k and 'F' in boxes[k] and k != i:
                    boxes[k][boxes[k].index('F')] = 'T'
    check = ['T' in item for item in boxes]
    return all(check)
