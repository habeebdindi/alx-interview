#!/usr/bin/python3
"""This module contains a function"""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened"""

    [box.append('F') for box in boxes[1:]]
    boxes[0].append('T')

    for i in range(len(boxes)):
        for key in boxes[i]:
            if isinstance(key, str):
                continue
            if (key < len(boxes) and boxes[key][-1] == 'F' and key != i):
                boxes[key][-1] = 'T'
    check = ['T' in item for item in boxes]
    return all(check)


"""
def canUnlockAll(boxes):

        canUnlockAll:
            this function check if all boxes can be unlocked

        Args:
            boxes (array): a box with keys to other boxes

        Returns:
            boolean: returns True if all boxes can be opened or else false


    visited = {0}
    keys = boxes[0]

    while keys:
        new_keys = []
        for key in keys:
            if key < len(boxes) and key not in visited:
                visited.add(key)
                new_keys.extend(boxes[key])

        keys = new_keys

    return len(visited) == len(boxes)
"""
