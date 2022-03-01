import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 위, 아래, 왼쪽, 오른쪽
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move(color, pos, d, board):
    r, c = pos
    board[r][c] = "."
    while 1:
        next_position = board[r + dr[d]][c + dc[d]]
        if next_position == ".":
            r += dr[d]
            c += dc[d]
        elif next_position == "O":
            return (-1, -1), board
        else:
            board[r][c] = color
            return (r, c), board


def first_second_move(d, red_pos, blue_pos):
    # 위 - 아래 - 왼쪽 - 오른쪽
    first, second = "R", "B"
    if d == 0:
        if red_pos[0] > blue_pos[0]:
            first, second = "B", "R"
    elif d == 1:
        if red_pos[0] < blue_pos[0]:
            first, second = "B", "R"
    elif d == 2:
        if red_pos[1] > blue_pos[1]:
            first, second = "B", "R"
    else:
        if red_pos[1] < blue_pos[1]:
            first, second = "B", "R"
    return first, second


def func(turn: int, board: list, d: int, red_pos, blue_pos) -> int:
    # 종료 조건
    if turn == 11 or blue_pos == (-1, -1):
        return 0
    if red_pos == (-1, -1):
        return 1

    first, second = first_second_move(d, red_pos, blue_pos)
    if first == "R":
        red_pos, board = move("R", red_pos, d, board)
        blue_pos, board = move("B", blue_pos, d, board)
    else:
        blue_pos, board = move("B", blue_pos, d, board)
        red_pos, board = move("R", red_pos, d, board)

    for i in range(4):
        if i == d:
            continue
        copy_board = [i[:] for i in board]
        ret = func(turn + 1, copy_board, i, red_pos, blue_pos)
        if ret:
            return 1
    return 0


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

for r in range(N):
    for c in range(M):
        if board[r][c] == "R":
            red_pos = (r, c)
        elif board[r][c] == "B":
            blue_pos = (r, c)

flag = 0
for d in range(4):
    copy_board = [i[:] for i in board]
    flag = func(0, copy_board, d, red_pos, blue_pos)
    if flag:
        break
print(flag)

