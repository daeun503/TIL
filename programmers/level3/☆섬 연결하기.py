# 이거 잘 못 풀었음 다시 풀기

# kruskal 속도1
# https://it-garden.tistory.com/411 보고함
def solution(n, costs):
    # union-find 연산 
    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]
    
    def union(a, b):
        root1 = find(a)
        root2 = find(b)
        p[root2] = root1
        
    costs.sort(key = lambda x: x[2])
    mst = []
    p = [i for i in range(n)]    # 각 정점은 자신이 대표
    
    mst_cost = 0
    tree_edges = 0
    while tree_edges != n-1:     # 간선이 n-1개 연결되면 끝
        v, w, wt = costs.pop(0)
        if find(v) != find(w):   # 서로소면
            union(v, w)          # 집합 합치기
            mst.append((v, w))   # 경로 추가
            mst_cost += wt       # 가중치 추가
            tree_edges += 1      # 간선 개수 +1
    return mst_cost 

    
# Dijkstra 속도2
def solution(n, costs):
    INF = 9999999
    cost = [INF] * n
    visited = [0] * n

    G = [[INF] * n for _ in range(n)]
    for v, w, c in costs:
        G[v][w] = c
        G[w][v] = c
    
    def Dijkstra(v):
        island = [v]              # 이동하는 순서
        cost[v] = 0               # 시작 지점은 0
        while len(island) < n:
            v = island[-1]        # 출발점 v
            visited[v] = 1        # 방문 표시
            for w in range(n):
                # 도착지 w에 아직 방문하지 않았고, v~w 비용이 이전에 킵해둔 것보다 적으면 갱신
                if not visited[w] and cost[w] > G[v][w]:
                    cost[w] = G[v][w]
                    
            # cost리스트에서 가장 작은 cost로 이동할 수 있는 인덱스 찾기
            min_value, min_idx = INF, INF
            for idx, value in enumerate(cost):
                if idx not in island and min_value > value:
                    min_value, min_idx = value, idx
            island.append(min_idx)  # 해당 인덱스로 이동        
        return sum(cost)
    
    return Dijkstra(0)


# prim(더 잘 짜는게 있을 것 같다) 속도3
def solution(n, costs): 
    # 인접행렬
    G = [[9999999] * n for _ in range(n)]
    for v, w, c in costs:
        G[v][w] = c
        G[w][v] = c
    
    def prim(v):
        island = [v]        # 순회하는 순서
        visited = [0] * n   # 방문체크
        visited[v] = 1
        result = 0
        while len(island) != n:  # 모두 다 순회할 때 까지 반복
            tmp = 9999999
            for v in island:
                for w in range(n):
                    # 아직 방문하지 않았고, 간선의 비용이 가장 작을 때
                    if not visited[w] and G[v][w] < tmp:
                        tmp = G[v][w]  # 가장 작은 간선의 비용 갱신
                        target = w     # 그 때의 도착지 target
            island.append(target)  # 순서에 target을 넣고
            result += tmp          # 간선 비용 더해주기
            visited[target] = 1    # 방문체크
        return result
    
    return prim(0)