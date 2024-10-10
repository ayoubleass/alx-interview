#!/usr/bin/python3
"""
This module has canUnlockAll function  that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    Return boolean
    """
    foundKeys = set()
    explore = [0]
    while True:
        current_box = explore.pop()
        if current_box in foundKeys:
            continue 
        foundKeys.add(current_box)
        for key in boxes[current_box]:
            if key not in foundKeys and key < len(boxes):
                explore.append(key)
        if len(foundKeys) == len(boxes):
            break
        if not explore:
            break 
     return len(foundKeys) == len(boxes)
