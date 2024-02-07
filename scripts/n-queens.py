#!/usr/bin/python3
""" a program that solves the N queens problem.
"""
import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, row):
    if row == len(board):
        print_solution(board)
        return True
    
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1)
            board[row][col] = 0

def print_solution(board):
    for row in board:
        print("".join('Q' if cell == 1 else '.' for cell in row))
    print()

def solve_nqueens(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0] * n for _ in range(n)]
    solve_nqueens_util(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solve_nqueens(sys.argv[1])
