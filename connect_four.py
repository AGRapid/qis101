#!/usr/bin/env python3
"""connect_four.py"""

# Used Dr. David Biersach's code. attempted to understand
# what each function and command was doing.


def find_four(board: list[list[int]], row: int, col: int) -> bool:
    """This function will look for four of the same values in a row, column, or diagonal"""

    # You can win three ways with a ray pointing upwards...

    if (
        row > 2
    ):  # checking if at least 3 rows above the board so there is space to form a diagonal
        # This is upward to the right (diagonal)
        if col < 4 and (
            board[row][col] == board[row - 1][col + 1]
            and board[row][col] == board[row - 2][col + 2]
            and board[row][col] == board[row - 3][col + 3]
        ):  # col < 4 makes sure a diagonal is possible with at least 3 positions to the right
            return True

        # The is upward to the left (diagonal)
        if col > 2 and (
            board[row][col] == board[row - 1][col - 1]
            and board[row][col] == board[row - 2][col - 2]
            and board[row][col] == board[row - 3][col - 3]
        ):  # col<2 makes sure there is at least 3 positions from the left for the diagonal
            return True

        # This is straight up because the row is the only adjusted value
        if (
            board[row][col] == board[row - 1][col]
            and board[row][col] == board[row - 2][col]
            and board[row][col] == board[row - 3][col]
        ):
            return True

    # There can also be ways to win downward...

    if (
        row < 3
    ):  # Ensuring there are at least 3 rows below the top of the board to make a downward ray
        # This is downward to the right
        if col < 4 and (
            board[row][col] == board[row + 1][col + 1]
            and board[row][col] == board[row + 2][col + 2]
            and board[row][col] == board[row + 3][col + 3]
        ):  # col < 4 makes sure there is at least 3 spaces from the right
            return True
        # This is downward to the left
        if col > 2 and (
            board[row][col] == board[row + 1][col - 1]
            and board[row][col] == board[row + 2][col - 2]
            and board[row][col] == board[row + 3][col - 3]
        ):  # col > 2 makes sure there is 3 columns from the left of the board
            return True

        # This would be straight down as the row is the only adjusted value ( positive now )
        if (
            board[row][col] == board[row + 1][col]
            and board[row][col] == board[row + 2][col]
            and board[row][col] == board[row + 3][col]
        ):
            return True

    # This is horizontal to the right since the column is the only adjusted value and added to
    if col < 4 and (
        board[row][col] == board[row][col + 1]
        and board[row][col] == board[row][col + 2]
        and board[row][col] == board[row][col + 3]
    ):  # col < 4 ensures there are at least three spaces from the right to connect four
        return True

    # This is horizontal to the left since the column is subtracted
    if col > 2 and (
        board[row][col] == board[row][col - 1]
        and board[row][col] == board[row][col - 2]
        and board[row][col] == board[row][col - 3]
    ):  # col < 2 makes sure there is at least 3 spaces from the left
        return True
    return False


def check_winner(player: int, board: list[list[int]]) -> bool:
    """This function will run the find_four function to identify a winner"""
    for row in range(6):  # iterating over the row
        for col in range(7):  # iterating over the columns
            if board[row][col] == player and find_four(board, row, col):
                # board[row][col] checks the position and if found pattern, returns true
                return True
    return False


def print_winner(board: list[list[int]]) -> None:
    print(*board, sep="\n")
    if check_winner(1, board):
        print("Player 1 wins!")
    else:
        if check_winner(2, board):
            print("Player 2 wins!")
        else:
            print("No winner yet")
    print()


def main() -> None:
    board1: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]
    print_winner(board1)

    board2: list[list[int]] = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]
    print_winner(board2)

    board3: list[list[int]] = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    print_winner(board3)


if __name__ == "__main__":
    main()
