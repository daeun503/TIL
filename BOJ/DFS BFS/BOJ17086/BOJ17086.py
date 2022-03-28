import sys
nput = sys.stdin.readline
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [0, -1, 1, -1, 1, 0, -1, 1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

q = []
for r in range(N):
    for c in range(M):
        if board[r][c]:
            q.append((r, c))

while q:
    r, c = q.pop(0)
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not board[nr][nc]:
            board[nr][nc] = board[r][c] + 1
            q.append((nr, nc))

result = max(map(max, board))
print(result - 1)
