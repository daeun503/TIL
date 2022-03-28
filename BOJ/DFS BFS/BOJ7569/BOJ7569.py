import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

from collections import deque
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]


def bfs(red):
    q = deque(red)
    ret = 1
    while q:
        h, r, c = q.popleft()
        for i in range(6):
            nh = h + dh[i]
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and 0 <= nh < H and not IN[nh][nr][nc]:
                q.append((nh, nr, nc))
                IN[nh][nr][nc] = IN[h][r][c] + 1
                ret = IN[nh][nr][nc]
    return ret


def result(ret):
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if not IN[h][r][c]:
                    return -1

    return ret - 1


M, N, H = map(int, input().split())
IN = []
for _ in range(H):
    tmp = [list(map(int, input().split())) for _ in range(N)]
    IN.append(tmp)

red = []
for h in range(H):
    for r in range(N):
        for c in range(M):
            if IN[h][r][c] == 1:
                red.append((h, r, c))

print(result(bfs(red)))
