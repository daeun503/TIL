import sys
import heapq
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


def dijkstra(s):
    v = s
    dist[v], check[v] = 0, 1

    while not check[N]:

        # 방문하지 않은 노드들 중 dist 값이 가장 작은 노드를 선택해서 출발
        min_dist = 9999
        for i in range(N+1):
            if not check[i] and min_dist > dist[i]:
                min_dist = dist[i]
                v = i

        # 선택된거니까 체크
        check[v] = 1

        # v에서 w로 갈 수 있고, 아직 w에서 출발한 적 없으면
        # 원래 dist값이랑 v를 경유해서 가는 값이랑 비교해서 최솟값 갱신
        for w in range(N+1):
            if G[v][w] and not check[w]:
                dist[w] = min(dist[w], dist[v]+G[v][w])
    return dist[N]



for tc in range(1, int(input())+1):
    # N 시작 E 도착 최단거리는?
    N, E = map(int, input().split())
    dist = [999999] * (N+1)
    check = [0] * (N+1) # mst 정점 추가 여부

    # 인접 행렬
    G = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, weight = map(int, input().split())
        G[s][e] = weight

    print("#{} {}".format(tc, dijkstra(0)))

    heapq.