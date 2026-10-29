def board_text(board):
    rows = []
    for row in range(3):
        start = row * 3
        rows.append(" | ".join(board[start:start + 3]))
    return "\n---------\n".join(rows)
 
 
def winner(board):
    winning_lines = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )
    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c]:
            return board[a]
    return None
 
 
board = [str(number) for number in range(1, 10)]
player = "X"
 
while True:
    print(board_text(board))
    move = input(f"{player}, choose a square (1-9): ").strip()
 
    if not move.isdigit() or not 1 <= int(move) <= 9:
        print("Choose a number from 1 to 9.")
        continue
 
    square = int(move) - 1
    if board[square] in ("X", "O"):
        print("That square is taken.")
        continue
 
    board[square] = player
    current_winner = winner(board)
 
    if current_winner:
        print(board_text(board))
        print(f"{current_winner} wins.")
        break
    if all(value in ("X", "O") for value in board):
        print(board_text(board))
        print("Draw.")
        break
 
    player = "O" if player == "X" else "X"