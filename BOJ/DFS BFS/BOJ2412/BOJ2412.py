import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

import sys
input = sys.stdin.readline


def bfs():
    r, c = 0, 0
    visited[r][c] = 1
    q = [(r, c)]
    while q:
        r, c = q.pop(0)
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                nr = r + dr
                nc = c + dc
                # 범위 안, 홈이 있으면
                if (0 <= nr < R and 0 <= nc < C) and matrix[nr][nc] and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1
                    # 정상에 도달하면 리턴
                    if nc >= T:
                        return visited[nr][nc]
    # 정상 도달 못하면 -1
    return 0


n, T = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(n)]
R, C = max(map(max, IN)) + 1, T+1

matrix = [[0] * C for _ in range(R)]
visited = [[0] * C for _ in range(R)]

for item in IN:
    x, y = item
    matrix[x][y] = 1

# 처음 방문 체크 시작이 1이라 1 빼주기, 못 도달하면 0리턴 해서 -1 출력
result = bfs()
print(result - 1)
