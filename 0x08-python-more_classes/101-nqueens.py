#!/usr/bin/python3
"""
N-Queens Problem Solver
Usage: nqueens N
"""


import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n):
    """
    Utilizes backtracking to solve the N-Queens puzzle.
    """
    if col >= n:
        print(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, n) or res
            board[i][col] = 0

    return res


def solve_nqueens(n):
    """
    Solves the N-Queens puzzle for a given board size N.
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nqueens_util(board, 0, n):
        print("No solution exists")
        sys.exit(1)