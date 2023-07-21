#!/usr/bin/env python3
"""board_encoding.py"""

# Integer Representation of a Tic Tac Toe Board
# Used Chat GPT to assist in the decoding function


def decode_board(num: int) -> None:
    """This function will create the Board and decode
    an integer representation of a board."""

    # A Tic_Tac-Toe board is a 3 by 3 grid
    rows = 3
    columns = 3

    # Grid is initialized to zero. Zero's represent empty spaces
    grid: list[list[int]] = [[0] * columns for _ in range(rows)]

    n: int = num

    for row in range(rows):
        for column in range(columns):
            # modulus operator here is being used to calculate the remainder by dividing
            # a base of 3
            val = n % 3

            # assigning quotient to n
            n //= 3

            # If the value is 1, the position will represent an X
            if val == 1:
                grid[row][column] = "X"

            # Else if the value is 2, the position will represent an O
            elif val == 2:
                grid[row][column] = "O"

            # If the value is not a 1 or 2, the position will represent an open space
            else:
                grid[row][column] = " "

    return grid


def main() -> None:
    """This function defines the integer values and prints the grids"""
    num: int = 2271
    num2: int = 1638
    num3: int = 12065

    # Defining the boards
    board1: None = decode_board(num)
    board2: None = decode_board(num2)
    board3: None = decode_board(num3)

    # iterating over the rows, enumerating the board to get the indexes
    for i, row in enumerate(board1):
        # printing the row and separating each column with a "|"
        print(" | ".join(str(cell) for cell in row))

        # This creates a dashed line for each row ensuring only two dashed lines
        if i < len(board1) - 1:
            print("-" * 9)

    # This random print function is an attempt to add vertical space between boards.
    print()

    for i, row in enumerate(board2):
        print(" | ".join(str(cell) for cell in row))
        if i < len(board2) - 1:
            print("-" * 9)

    print()

    for i, row in enumerate(board3):
        print(" | ".join(str(cell) for cell in row))
        if i < len(board3) - 1:
            print("-" * 9)


if __name__ == "__main__":
    main()
