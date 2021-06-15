import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


def dijkstra(s, e):
    dist[s] = 0
    check_num = 0
    while not check[e]:

        # 선택 안 된 정점들 중 dist가장 짧은 거 선택
        unselected = [idx for idx, val in enumerate(check) if not val]
        v = min(unselected, key=lambda x: dist[x])

        check[v] = 1
        check_num += 1

        for w, weight in G[v]:
            if not check[w] and dist[w] > dist[v]+weight:
                dist[w] = dist[v] + weight
    return dist[e]

def dijkstra2(s):
    dist[s] = 0
    check_num = 0
    while check_num != N:

        # 선택 안 된 정점들 중 dist가장 짧은 거 선택
        unselected = [idx for idx, val in enumerate(check) if not val]
        v = min(unselected, key=lambda x: dist[x])

        check[v] = 1
        check_num += 1

        for w, weight in G[v]:
            if not check[w] and dist[w] > dist[v]+weight:
                dist[w] = dist[v] + weight



# 각 마을에서 X까지 최단거리로 오고 -> 스타트 각 마을
# X에서 각 마을로 최단거리로 가면 됨 -> 스타트 X
# -> for문으로 모든 정점에서 다익스트라

N, M, X = map(int, input().split())

# # 인접 행렬 시간초과
# G = [[0]*(N+1) for _ in range(N+1)]
# for _ in range(M):
#     s, e, weight = map(int, input().split())
#     G[s][e] = weight

# 인접 리스트로 하면 인접행렬보다 많이 가긴 하는데 그래도 시간초과
G = [[]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, weight = map(int, input().split())
    G[s].append((e, weight))

# s에서 출발해서 X에 도착하는 최단 거리
result = [0] * (N+1)
for s in range(1, N+1):
    dist = [999999999] * (N + 1)
    check = [0] * (N + 1)
    if s != X:
        result[s] += dijkstra(s, X) # s출발 X도착
    else:
        dijkstra2(X)  # X 출발한 결과로 마지막 얻은 dist를 사용
        for e in range(1, N + 1):
            result[e] += dist[e]

# 출력
print(max(result))