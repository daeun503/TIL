import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

'''
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    p[find(y)] = find(x)

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    IN = [list(map(int, input().split())) for _ in range(E)]
    IN.sort(key = lambda x : x[2])  # 가중치를 기준으로 정렬
    p = [i for i in range(V + 1)]   # 각 정점의 대표는 자기 자신

    # 크루스칼
    edge_cnt = 0
    mst_cnt = 0
    while edge_cnt != V:         # 정점이 V+1개, 간선이 V개
        n1, n2, w = IN.pop(0)
        if find(n1) != find(n2):  # 서로 다른 집합이면
            union(n1, n2)         # 연결해주고
            edge_cnt += 1         # 간선 카운트 +1
            mst_cnt += w          # 간선 가중치 mst에 추가

    print("#{} {}".format(tc, mst_cnt))

'''
########################################################################################
# 프림
def prim(s):
    dist[s] = 0
    mst_num = 0
    while mst_num != V+1:
        # # 아직 가지 않은 곳에서 최소 거리인 정점 선택
        unselected = [idx for idx, val in enumerate(mst) if not val]
        v = min(unselected, key=lambda x: dist[x])

        # mst 정점에 추가
        mst[v] = 1
        mst_num += 1

        # 기존에 갖고 있던 거리 정보와 v->w 거리 정보와 비교해서 최솟값 갱신
        for w in range(V+1):
            if G[v][w] and not mst[w]:
                dist[w] = min(dist[w], G[v][w])

    return


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    # 인접 행렬 만들기
    G = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b, w = map(int, input().split())
        G[a][b] = w
        G[b][a] = w

    # 거리 정보
    dist = [9999999999] * (V+1)
    # mst 정보
    mst = [0] * (V+1)

    print("#{} {}".format(tc, prim(0)))
