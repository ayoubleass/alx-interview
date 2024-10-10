#!/usr/bin/python3
"""
This module has canUnlockAll function
that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened and returns boolean
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if ((type(boxes)) is not list 
    or (len(boxes)) == 0):
        return False
    foundKeys = set()
    explore = [0]
    while explore:
        current_box = explore.pop()
        if current_box in foundKeys:
            continue 
        foundKeys.add(current_box)
        for key in boxes[current_box]:
            if (key not in foundKeys 
            and key < len(boxes)):
                explore.append(key)
    return len(foundKeys) == len(boxes)
