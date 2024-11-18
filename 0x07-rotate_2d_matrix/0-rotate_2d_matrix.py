#!/usr/bin/python3
"""
This module has the rotate_2d_matrix function
which rotate a matrix 90 degrees clockwise.
"""
import copy


def rotate_2d_matrix(matrix):
    """
    Rotates n x n 2D matrix 90 degrees clockwise.
    """
    n = len(matrix)
    temp = copy.deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            matrix[j][i] = temp[n - i - 1][j]
