# Tic-Tac-Toe Game

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                raise ValueError("Move must be between 1 and 9.")
            return divmod(move, 3)  # Convert 1D index to 2D coordinates
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Player {players[current_player]}'s turn.")
        while True:
            row, col = get_move()
            if board[row][col] == " ":
                board[row][col] = players[current_player]
                break
            else:
                print("Cell already taken. Choose another.")

        print_board(board)

        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        current_player = 1 - current_player  # Switch player


if __name__ == "__main__":
    main()
