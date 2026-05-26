
# Sudoku Board
# 0 means empty space

board = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,0,8],
    [1,9,8,3,4,2,0,6,7],

    [8,5,9,7,6,1,4,0,3],
    [4,2,6,8,5,3,0,9,1],
    [7,1,3,9,2,4,0,0,6],

    [9,6,1,5,3,7,2,8,0],
    [2,8,7,4,1,9,0,0,5],
    [3,4,5,2,8,6,1,7,9]
]


# Function to print the board properly
def print_board(board):

    for i in range(9):

        # Print horizontal line after every 3 rows
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(9):

            # Print vertical line after every 3 columns
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(board[i][j], end=" ")

        print()


# Function to check whether a number can be placed
def is_valid(board, row, col, num):

    # Check Row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check Column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 Box

    # Find top-left corner of box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    # Loop through box
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):

            if board[i][j] == num:
                return False

    return True


# Main Game Loop
while True:

    print("\nCurrent Sudoku Board:\n")
    print_board(board)

    # Take user input
    row = int(input("\nEnter row (0-8): "))
    col = int(input("Enter column (0-8): "))
    num = int(input("Enter number (1-9): "))

    # Check if cell is already filled
    if board[row][col] != 0:
        print("Cell already filled!")
        continue

    # Validate move
    if is_valid(board, row, col, num):

        board[row][col] = num
        print("Number inserted successfully!")

    else:
        print("Invalid move!")

    # Check if game completed
    completed = True

    for i in range(9):
        for j in range(9):

            if board[i][j] == 0:
                completed = False

    if completed:
        print("\nCongratulations! Sudoku Solved!")
        print_board(board)
        break