import sys
sys.stdin = open("input.txt", "r")


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(s):
    matrix[s[0]][s[1]] = 0
    q = [s]
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc]:
                q.append((nr, nc))
                matrix[nr][nc] = 0


def dfs(s):
    matrix[s[0]][s[1]] = 0
    q = [s]
    while q:
        r, c = q.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc]:
                q.append((nr, nc))
                matrix[nr][nc] = 0


for _ in range(int(input())):
    C, R, K = map(int, input().split())
    matrix = [[0] * C for _ in range(R)]
    for _ in range(K):
        c, r = map(int, input().split())
        matrix[r][c] = 1

    result = 0
    for r in range(R):
        for c in range(C):
            if matrix[r][c] == 1:
                bfs((r, c))
                result += 1

    print(result)
