import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

# 남동북서
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 시작 지점에서 어딘가 뚫려 있으면 큐에 넣기
# 서 0001 / 북 0010 / 동 0100 / 남 1000
def bfs(s: tuple, num: int):
    r, c = s
    visited[r][c] = num
    q = [s]
    room_scale = 1

    while q:
        r, c = q.pop(0)
        # 4bit 2진수로 변경
        tmp = bin(wall[r][c])[2:]
        dec_to_bin = "0" * (4 - len(tmp)) + tmp
        # 4bit 2진수를 순서대로 확인
        for idx, i in enumerate(dec_to_bin):
            # 벽이 있으면 그냥 통과
            if int(i):
                continue

            # 벽이 없으면 nr, nc를 구한다.
            nr = r + dr[idx]
            nc = c + dc[idx]
            if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = num
                q.append((nr, nc))
                room_scale += 1

    return room_scale


N, M = map(int, input().split())
wall = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

# 아직 방문하지 않은 곳을 찾으면 bfs
num, rooms_scale = 1, [0]
for r in range(M):
    for c in range(N):
        if not visited[r][c]:
            rooms_scale.append(bfs((r, c), num))
            num += 1

# 벽 하나 없애기
remove_wall = 0
for r in range(M):
    for c in range(N):
        # 아래쪽 벽 지우기
        if r+1 < M and visited[r][c] != visited[r+1][c]:
            a, b = visited[r][c], visited[r+1][c]
            remove_wall = max(remove_wall, rooms_scale[a] + rooms_scale[b])
        # 오른쪽 벽 지우기
        if c+1 < N and visited[r][c] != visited[r][c+1]:
            a, b = visited[r][c], visited[r][c+1]
            remove_wall = max(remove_wall, rooms_scale[a] + rooms_scale[b])

print(num - 1)
print(max(rooms_scale))
print(remove_wall)
