import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


# 이건 메모리 안터지네
# 프림
def prim(s):
    dist[s] = 0
    mst_num = 0
    while mst_num != V:
        # # 아직 가지 않은 곳에서 최소 거리인 정점 선택
        unselected = [idx for idx, val in enumerate(mst) if not val]
        v = min(unselected, key=lambda x: dist[x])

        # mst 정점에 추가
        mst[v] = 1
        mst_num += 1

        # 기존에 갖고 있던 거리 정보와 v->w 거리 정보와 비교해서 최솟값 갱신
        for w in range(1, V+1):
            if G[v][w] and not mst[w]:
                dist[w] = min(dist[w], G[v][w])
    return sum(dist[1:])


V = int(input())
E = int(input())

# 인접 행렬 만들기 무방향인지 방향인지 잘 봐야함 이걸로 삽질했다..
G = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    G[a][b] = w
    G[b][a] = w

# 거리 정보
dist = [9999999999] * (V+1)
# mst 정보
mst = [0] * (V+1)

print(prim(1))


#######################################################################
# 크루스칼
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    p[find(y)] = find(x)

def kruskal():
    edge_num = 0
    mst_w = 0
    while edge_num != N-1:
        a, b, w = IN.pop(0)
        if find(a) != find(b):
            union(a, b)
            mst_w += w
            edge_num += 1
    return mst_w

N = int(input())
M = int(input())
IN = [list(map(int, input().split())) for _ in range(M)]
IN.sort(key = lambda x : x[2])
p = [i for i in range(N+1)]
print(kruskal())