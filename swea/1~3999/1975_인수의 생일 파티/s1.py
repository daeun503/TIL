import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

import heapq

def dijkstra(G, s):
    dist = [999999999] * (N + 1)
    dist[s] = 0

    q = []
    heapq.heappush(q, (0, s))
    while q:
        weight, v = heapq.heappop(q)
        for w in range(1, N+1):
            if G[v][w] and G[v][w]+dist[v] < dist[w]:
                dist[w] = G[v][w]+dist[v]
                heapq.heappush(q, (dist[w], w))

    return dist[1:]


for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())

    G_go = [[0]*(N+1) for _ in range(N+1)]
    G_back = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b, w = map(int, input().split())
        G_go[a][b] = w
        G_back[b][a] = w

    go_X = dijkstra(G_go, X)
    from_X = dijkstra(G_back, X)

    result = [a+b for a, b in zip(go_X, from_X)]
    print("#{} {}".format(tc, max(result)))