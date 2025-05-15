def print_board(board):
    """打印棋盘"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """检查是否有玩家获胜"""
    # 检查行和列 
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True

    # 检查对角线
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def is_draw(board):
    """检查是否平局"""
    return all([cell != " " for row in board for cell in row])


def play_tic_tac_toe():
    """主游戏逻辑"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        try:
            row, col = map(int, input(f"玩家 {player} 的回合，请输入行和列（0-2）：").strip().split())
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("无效的行或列，请输入0到2之间的数字。")
                continue
            if board[row][col] != " ":
                print("该位置已被占用，请选择其他位置。")
                continue
        except ValueError:
            print("输入无效，请输入两个数字，用空格分隔。")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"玩家 {player} 获胜！")
            break

        if is_draw(board):
            print_board(board)
            print("平局！")
            break

        turn += 1


if __name__ == "__main__":
    print("欢迎来到三子棋游戏！")
    play_tic_tac_toe()