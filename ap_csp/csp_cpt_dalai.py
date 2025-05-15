board = {
    "a1": "#", "a2": "#", "a3": "#",
    "b1": "#", "b2": "#", "b3": "#",
    "c1": "#", "c2": "#", "c3": "#"
}

def display(board):
    print(board["a1"], board["a2"], board["a3"])
    print(board["b1"], board["b2"], board["b3"])
    print(board["c1"], board["c2"], board["c3"])

def check_winner(player):
    win_combos = [
        ["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"],
        ["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"],
        ["a1", "b2", "c3"], ["a3", "b2", "c1"]
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def gameplay():
    current_player = "X"
    moves = 0

    while moves < 9:
        display(board)
        move = input("Player " + current_player + ", your move (a1 - c3): ").lower()

        if move in board:
            if board[move] == "#":
                board[move] = current_player
                moves += 1

                if check_winner(current_player):
                    display(board)
                    print("Player " + current_player + " wins!")
                    return

                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"
        else:
            print("That spot is already taken. Try again.")
    display(board)
    print("It's a draw!")

gameplay()