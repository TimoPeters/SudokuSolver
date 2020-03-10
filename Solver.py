# Created by Timo Peters
# Date: 25.02.2020

# This programm solves every Sudoku puzzle. It uses a simple recursive backtracking algorithm.
# A Sudoku board is represented by a 2 dimensional array
# Call the start method and give it the board you want to solve as parameter (start(<Board>)) (fE start(board2))
# The origin board will be printed first and the solved version a few seconds later
# (depending on how complex the puzzle is)

# Sudoku rules:
# A Sudoku puzzle finds place on a 9x9 board with just some spaces containing a number from 1-9
# The players job is it to fill all the empty spaces
# Each row, column and 3x3 box must only contain each number from 1-9 once
# Once there are no empty spaces and there are no invalid numbers the puzzle is solved

# Represents a 9x9 Sudoku board
# 0 stands for an empty space
board1 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Hardest Sudoku in the world. Source: https://www.oe24.at/welt/Das-ist-das-schwierigste-Sudoku-der-Welt/1597831
board2 = [
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 7, 0, 0, 1, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 5, 3, 0, 0],
    [0, 1, 0, 0, 7, 0, 0, 0, 6],
    [0, 0, 3, 2, 0, 0, 0, 8, 0],
    [0, 6, 0, 5, 0, 0, 0, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 9, 7, 0, 0]
]

board3 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# Prints the board in the console
def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")

        for col in range(len(board)):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")


# Finds the next empty space on the board
def find_next_empty(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return row, col
    return None


# Checks if the new entry at board[i][j] is valid
def is_valid(row, col, num, board):
    # Check row
    for j in range(len(board)):
        if num == board[row][j] and col != j:
            return False

    # Check column
    for i in range(len(board)):
        if num == board[i][col] and row != i:
            return False

    # Check box
    box_row = row // 3
    box_col = col // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if num == board[i][j] and (row != i or col != j):
                return False
    return True


# Solves the Sudoku puzzle by using a backtracking algorithm
def solve(board):
    next_empty = find_next_empty(board)
    if not next_empty:
        return True
    else:
        row, col = next_empty

    for i in range(1, 10):
        if is_valid(row, col, i, board):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


# Start the solver
def start(board):
    print_board(board)
    solve(board)
    print("____________________________________________________________________________\n")
    print_board(board)


start(board2)
