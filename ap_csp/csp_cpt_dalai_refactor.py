# 声明一个棋盘，3x3 的棋盘，使用字典来表示，初始值为 #，代表棋盘上每个位置都没有棋子
board = {
    "a1": "#", "a2": "#", "a3": "#",
    "b1": "#", "b2": "#", "b3": "#",
    "c1": "#", "c2": "#", "c3": "#"
}

# 展示 3x3 棋盘上每个位置的棋子
def display(board):
    print(board["a1"], board["a2"], board["a3"])
    print(board["b1"], board["b2"], board["b3"])
    print(board["c1"], board["c2"], board["c3"])

# 在每次有玩家下一步棋的时候即 invoke make_move()，检查当前下棋的 player 是否满足胜利条件
# 列举出所有可能的胜利组合
# 1. 横向
# 2. 纵向
# 3. 斜向
# 4. 反斜向
# 然后遍历每种组合中的三个位置的棋子是否都相同，且棋子是当前玩家下的
def check_winner(board, player):
    win_combos = [
        ["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"],
        ["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"],
        ["a1", "b2", "c3"], ["a3", "b2", "c1"]
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# 玩家下棋，board: 棋盘，player: 是当前下棋的玩家，move: 是玩家下棋的位置
# 检查下棋的位置是否在棋盘上，且该位置没有棋子
# 如果满足条件，则在该位置上放置当前玩家的棋子，返回 True
# 否则返回 False
def make_move(board, player, move):
    if move in board and board[move] == "#":
        board[move] = player
        return True
    return False

# 切换当前下棋的玩家, 返回下一个玩家
# 如果当前玩家是 X，则切换为 O，否则切换为 X
# 这个函数可以在每次玩家下棋后调用
# 这样就可以在下棋的逻辑中不需要判断当前玩家是谁
def switch_player(current_player):
    return "O" if current_player == "X" else "X"

# 游戏的主逻辑
# 1. 初始化棋盘
# 2. 初始化当前玩家为 X
# 3. 初始化已经下的棋子数为 0
# 4. 循环直到下满 9 个棋子
# 5. 每次玩家下棋后，检查是否有玩家获胜
# 6. 如果有玩家获胜，则展示棋盘并打印获胜信息
# 7. 如果下满 9 个棋子，则展示棋盘并打印平局信息
# 8. 如果没有玩家获胜，则切换当前玩家
# 9. 如果玩家下棋的位置已经被占用，则提示玩家重新下棋
# 10. 如果玩家下棋的位置不在棋盘上，则提示玩家重新下棋
# 11. 如果玩家下棋的位置在棋盘上，但已经被占用，则提示玩家重新下棋
# 12. 如果玩家下棋的位置在棋盘上，且没有被占用，则在该位置上放置当前玩家的棋子
def gameplay(board):
    current_player = "X"
    moves = 0

    while moves < 9:
        display(board)
        move = input("Player " + current_player + ", your move (a1 - c3): ").lower()

        # 引起 run-time error，当输入时直接 enter, 此时输入的 move 是空字符串
        # 如果再通过 move[0] 取空字符串的第一个字符，则会报错 string index out of range
        if make_move(board, current_player, move[0]):
            moves += 1

            if check_winner(board, current_player):
                display(board)
                print("Player " + current_player + " wins!")
                return

            current_player = switch_player(current_player)
        else:
            print("That spot is already taken. Try again.")
    display(board)
    print("It's a draw!")

gameplay(board)

# 所有测试情况
# 1. 正常在 9 步之内结束，有玩家获胜
# 2. 正常在 9 步之内结束，平局

# Error Testing
# 有玩家输入不存在的棋盘位置
# 有玩家输入已经被占用的棋盘位置
