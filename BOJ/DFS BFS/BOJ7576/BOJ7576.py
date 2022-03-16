import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(red):
    q = deque(red)
    ret = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not IN[nr][nc]:
                q.append((nr, nc))
                IN[nr][nc] = IN[r][c] + 1
                ret = IN[nr][nc]
    return ret


def result(ret):
    for r in range(N):
        for c in range(M):
            if not IN[r][c]:
                return -1

    return ret - 1


M, N = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]

red = []
for r in range(N):
    for c in range(M):
        if IN[r][c] == 1:
            red.append((r, c))

print(result(bfs(red)))
