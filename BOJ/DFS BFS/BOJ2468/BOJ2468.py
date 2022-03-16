import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c, h):
    IN_copy[r][c] = 0
    q = [(r, c)]
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and IN_copy[nr][nc] > h:
                q.append((nr, nc))
                IN_copy[nr][nc] = 0


N = int(input())
IN = [list(map(int, input().split())) for _ in range(N)]

# 땅들 중에서 가장 높은 곳
max_h = max(map(max, IN))
# 가장 높은 곳 vs 비 최대값 => 비 높이 어디까지 볼지
rain_h = min(max_h+1, 101)

result = 0
for h in range(rain_h):
    h_result = 0
    IN_copy = [i[:] for i in IN]
    for r in range(N):
        for c in range(N):
            # r, c가 침수되지 않는 곳이면 침수 안되는 영역 bfs 확인
            if IN_copy[r][c] > h:
                bfs(r, c, h)
                h_result += 1
    result = max(result, h_result)

print(result)


