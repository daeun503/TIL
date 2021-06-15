def solution(n, edge):
    visited = [0] * (n+1)
    # 인접 행렬 만들기 (시간초과. bfs에서 pop(0) 바꿔도 해결x)
    # 인접 행렬 장점: 구현이 쉽다. O(1)로 접근 가능. 단, 노드의 수에 비해 간선의 수가 적으면 비효율적
    # G = [[0]*(n+1) for _ in range(n+1)] 
    # for v, w in edge:
    #     G[v][w] = 1
    #     G[w][v] = 1
    
    # 인접 리스트 만들기 
    # 인접 리스트 장점: 간선의 수에 비례하기 때문에 적은 메모리차지. 단, i와 j가 연결확인하기 위해 G[i] 다 봐야함
    G = [[] for _ in range(n+1)]
    for v, w in edge:
        G[v].append(w)
        G[w].append(v)
    
    # 이건 평범한 최단거리 bfs
    def bfs(s):
        q = [s]
        visited[s] = 1
        while q:
            v = q.pop(0)
            for w in set(G[v]): # 인접 리스트만들 때 중복 간선 있을 수도 있으니까 제외 
                if visited[w] == 0:
                    visited[w] = visited[v] + 1
                    q.append(w)
        max_d = max(visited)
        return visited.count(max_d)
    
    return bfs(1)