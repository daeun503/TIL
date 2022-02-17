import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 하, 상, 왼, 오
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def next_d(obj, d):
    # 왼 오만 방향 바뀜
    if obj == 1:
        next_d = [0, 1, 3, 2]
    # 상 하만 방향 바뀜
    elif obj == 2:
        next_d = [1, 0, 2, 3]
    # 모두 방향 바뀜
    elif obj == 3:
        next_d = [3, 2, 1, 0]
    # 모두 방향 바뀜
    else:
        next_d = [2, 3, 0, 1]

    return next_d[d]


def go(sr, sc, d):
    POS[sr][sc] = 1
    r, c, d = sr, sc, d
    while 1:
        nr = r + dr[d]
        nc = c + dc[d]
        nd = d

        # 범위 바깥이면 X
        if not (0 <= nr < N and 0 <= nc < M):
            return

        # 다시 에어컨자리로 오면 X
        if nr == sr and nc == sc:
            return

        # 범위 내
        POS[nr][nc] = 1
        # 물건 O
        if IN[nr][nc]:
            # 이미 와 본 물건 경로면 끝
            if Obj[nr][nc][nd]:
                return
            # 처음 와보면 go
            else:
                Obj[nr][nc][nd] = 1
                r, c = nr, nc
                d = next_d(IN[nr][nc], nd)

        # 물건 X => 다음 사이클
        else:
            r, c, d = nr, nc, nd


# n x m 행렬
N, M = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]
POS = [[0] * M for _ in range(N)]
Obj = [[[0] * 4 for _ in range(M)] for _ in range(N)]

# 에어컨 위치 찾기
aircons = []
for r in range(N):
    for c in range(M):
        if IN[r][c] == 9:
            aircons.append((r, c))

# 모든 에어컨들에서 탐색 => 4방향으로
while aircons:
    sr, sc = aircons.pop()
    POS[sr][sc] = 1
    for i in range(4):
        go(sr, sc, i)

# 앉을 수 있는 위치 개수 세기
result = 0
for j in range(N):
    result += sum(POS[j])

print(result)
