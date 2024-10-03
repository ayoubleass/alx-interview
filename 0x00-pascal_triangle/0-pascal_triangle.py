#!/usr/bin/python3
"""This module has a function that compute the pascals triangle"""


def pascal_triangle(n):
    """Return a pascals triangle"""
    pascal_trig = list()
    for i in  range(n):
        if(i == 0):
            pascal_trig.insert(i, [1])
        else :
            newList = list()
            newList.append(1)
            if len(pascal_trig[i - 1])  > 1 :
                for j in range(len(pascal_trig[i - 1])):
                    if (j + 1)  < len(pascal_trig[i - 1]):
                        num = pascal_trig[i - 1][j]
                        num2 = pascal_trig[i - 1][j + 1]
                        newList.append(num + num2)
            newList.append(1)
            pascal_trig.insert(i, newList)
    return pascal_trig
