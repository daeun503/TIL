import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


# 오른쪽, 왼쪽, 위, 아래
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def blue_trans_dir(d):
    if d == 0: return 1
    elif d == 1: return 0
    elif d == 2: return 3
    else: return 2


def move(idx, r, c, d, recursion=0):
    # 움직이려는 말이 맨 아래가 아니면 return
    if chess_map[r][c][0] != idx:
        return

    # 다음 이동할 칸 확인
    nr = r + dr[d]
    nc = c + dc[d]

    # 범위 벗어났을 때거나 파란 색이면
    if not (0 <= nr < N and 0 <= nc < N) or color_map[nr][nc] == 2:
        # 만약 이전 함수에서 재귀한거면 return
        if recursion:
            return
        # 재귀하지 않았던 거면 (첫 회차) 재귀
        d = blue_trans_dir(d)
        chess[idx][2] = d
        move(idx, r, c, d, 1)
        return

    # 흰색이면 다음 말 위에 그대로 얹고, 빨강이면 뒤집어서 얹기
    if color_map[nr][nc] == 0:
        chess_map[nr][nc].extend(chess_map[r][c])
    else:
        chess_map[nr][nc].extend(chess_map[r][c][::-1])
    # 이동한 말들 위치 정보 갱신해주기
    for idx in chess_map[r][c]:
        chess[idx][0], chess[idx][1] = nr, nc
    chess_map[r][c] = []


def finish_check():
    for r in range(N):
        for c in range(N):
            if len(chess_map[r][c]) >= 4:
                return 1
    return 0


N, K = map(int, input().split())
color_map = [list(map(int, input().split())) for _ in range(N)]
chess_map = [[[] for _ in range(N)] for _ in range(N)]
chess = []

for idx in range(K):
    r, c, d = map(int, input().split())
    chess.append([r-1, c-1, d-1])
    chess_map[r-1][c-1].append(idx)

count = 1
while count < 1001:
    # 말 하나씩 이동시키기
    for idx in range(K):
        r, c, d = chess[idx]
        move(idx, r, c, d)
    # 한 턴 끝났을 때 말 4개 이상 쌓였는지 체크
    if finish_check():
        break
    count += 1

if count == 1001:
    print(-1)
else:
    print(count)
