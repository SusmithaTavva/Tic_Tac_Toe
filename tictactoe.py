def print_board(board):
    # Function to print the Tic-Tac-Toe board
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Function to check if a player has won the game
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    # Function to check if the game is a draw
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    # Main game loop
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get the player's move
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))

        # Validate the move
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()
