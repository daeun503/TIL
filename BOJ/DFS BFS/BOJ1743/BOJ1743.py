import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    board[r][c] = 0
    count = 1
    q = [(r, c)]
    while q:
        r, c, = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc]:
                q.append((nr, nc))
                board[nr][nc] = 0
                count += 1
    return count


N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

result = 0
for r in range(N):
    for c in range(M):
        if board[r][c]:
            result = max(result, bfs(r, c))

print(result)
