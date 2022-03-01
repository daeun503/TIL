import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

# 상, 하, 좌, 우 -> 좌 우 상 하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = []

# init
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
visited[rx][ry][bx][by] = True
q.append((rx, ry, bx, by, 1)) # 위치 정보와 depth


def move(x, y, dx, dy):
    ctr = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        ctr += 1
    return x, y, ctr


def bfs():
    while q:
        rx, ry, bx, by, depth = q.pop(0)
        if depth > 10:
            break
        for i in range(4):
            rx_tmp, ry_tmp, r_ctr = move(rx, ry, dx[i], dy[i])
            bx_tmp, by_tmp, b_ctr = move(bx, by, dx[i], dy[i])
            # print(rx_tmp, ry_tmp, r_ctr, bx_tmp,by_tmp, b_ctr)

            if board[bx_tmp][by_tmp] == 'O':
                continue
            if board[rx_tmp][ry_tmp] == 'O':
                print(1)
                return
            if rx_tmp == bx_tmp and ry_tmp == by_tmp:
                if r_ctr > b_ctr:
                    rx_tmp -= dx[i]
                    ry_tmp -= dy[i]
                    r_ctr -= 1
                else:
                    bx_tmp -= dx[i]
                    by_tmp -= dy[i]
                    b_ctr -= 1
            if visited[rx_tmp][ry_tmp][bx_tmp][by_tmp] == False:
                visited[rx_tmp][ry_tmp][bx_tmp][by_tmp] = True
                q.append((rx_tmp,ry_tmp,bx_tmp,by_tmp,depth+1))
    print(0)

bfs()