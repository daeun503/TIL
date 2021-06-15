import sys
import heapq
sys.stdin = open("input.txt")
from pandas import DataFrame

import heapq

def dijkstra(s, e):
    dist[s] = 0

    q = []
    heapq.heappush(q, (0, s))

    while q:
        # 제일 작은 노드 선택
        current_dist, v = heapq.heappop(q)
        # 인접 정점들 중에서 아직 체크 안하고, dist[w]보다 경유하는게 더 짧으면
        for w, weight in G[v]:
            if dist[w] > dist[v] + weight:
                dist[w] = dist[v] + weight
                heapq.heappush(q, (dist[w], w))
    return dist[e]


N, M, X = map(int, input().split())

G = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, weight = map(int, input().split())
    G[s].append((e, weight))



# 각 마을에서 X까지 최단거리로 오고 -> 스타트 각 마을
# X에서 각 마을로 최단거리로 가면 됨 -> 스타트 X
# -> for문으로 모든 정점에서 다익스트라

# s에서 출발해서 X에 도착하는 최단 거리
result = [0] * (N+1)
for s in range(1, N+1):
    dist = [999999999] * (N + 1)
    check = [0] * (N + 1)
    if s != X:
        result[s] += dijkstra(s, X) # s출발 X도착
    else:
        dijkstra(X, 1)  # X 출발한 결과로 마지막 얻은 dist를 사용
        for e in range(1, N + 1):
            result[e] += dist[e]

# 출력
print(max(result))