import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

key_type = ["a", "b", "c", "d", "e", "f"]
door_type = ["A", "B", "C", "D", "E", "F"]

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

for r in range(N):
    for c in range(M):
        if maze[r][c] == "0":
            me = (r, c, 0)

visited = [[[0] * 64 for _ in range(M)] for _ in range(N)]
visited[me[0]][me[1]][me[2]] = 1
q = [me]
while q:
    r, c, k = q.pop(0)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        nk = k
        # 범위 바깥이거나, 벽이면 못 감
        if not (0 <= nr < N and 0 <= nc < M):
            continue

        # 벽이면 못 감
        if maze[nr][nc] == "#":
            continue
        # 출구면 끝
        elif maze[nr][nc] == "1":
            print(visited[r][c][k])
            exit()
        # 열쇠면 내 키에 추가
        elif maze[nr][nc] in key_type:
            nk |= 1 << (ord(maze[nr][nc]) - ord("a"))
        # 문인데, 키를 가지고 있지 않으면 못 감
        elif (maze[nr][nc] in door_type) and not (nk & (1 << ord(maze[nr][nc]) - ord("A"))):
            continue

        # 방문체크 안했으면 새로 써주기
        if not visited[nr][nc][nk]:
            q.append((nr, nc, nk))
            visited[nr][nc][nk] = visited[r][c][k] + 1
print(-1)

