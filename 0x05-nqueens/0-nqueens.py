#!/usr/bin/python3
"""
"""
import sys


def solve_n_queens(n):
    """
    Solves the N-Queens problem for a given board size.
    """
    def backtrack(col, pos_diagonal, neg_diagonal, board, row):
        if row == n:
            return [[board[i][:] for i in range(n)]]
        solutions = []
        for x in range(n):
            if x not in col and (x - row) not in neg_diagonal and (x + row) not in pos_diagonal:
                board[row][x] = 1
                col.add(x)
                neg_diagonal.add(x - row)
                pos_diagonal.add(x + row)
                solutions += backtrack(col,
                                       pos_diagonal,
                                       neg_diagonal, board, row + 1)
                board[row][x] = 0
                col.remove(x)
                neg_diagonal.remove(x - row)
                pos_diagonal.remove(x + row)

        return solutions
    board = [[0] * n for _ in range(n)]
    solutions = []
    solutions = backtrack(set(), set(), set(), board, 0)
    return solutions


def printSolution(n):
    """
    Display the solution as the example.
    """
    solutions = solve_n_queens(n)
    board = []
    result = ''
    for sol in solutions:
        board = sol
        result += '['
        for y in range(len(board)):
            for x in range(len(board)):
                if board[y][x] == 1:
                    result += "[{}, {}]".format(y, x)
                    if y < n - 1:
                        result += ', '
        result += ']\n'
    result = result[:len(result) - 1]
    print(result)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(n[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        printSolution(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
