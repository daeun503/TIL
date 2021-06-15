import sys
sys.stdin = open("input.txt")
from pandas import DataFrame
import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra():
    dist = [[9999999]*N for _ in range(N)]
    dist[0][0] = IN[0][0]

    q = []
    heapq.heappush(q, (IN[0][0], 0, 0))
    while q:
        w, r, c = heapq.heappop(q)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if dist[nr][nc] > dist[r][c] + IN[nr][nc]:
                    dist[nr][nc] = dist[r][c] + IN[nr][nc]
                    heapq.heappush(q, ((dist[nr][nc]), nr, nc))
    return dist[N-1][N-1]


for tc in range(1, int(input())+1):
    N = int(input())
    IN = [list(map(int, str(input()))) for _ in range(N)]
    print("#{} {}".format(tc, dijkstra()))