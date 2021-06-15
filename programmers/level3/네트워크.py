def solution(n, computers):
    visited = [0] * n
    cnt = 1
    
    def bfs(v):
        nonlocal cnt
        
        q = [v]                # bfs를 위한 큐
        visited[v] = cnt       # 몇 번째 네트워크 인가? 
        while q:               # 큐가 빌 때까지 반복
            v = q.pop(0)       # 큐에서 꺼내서 v로 
            for w in range(1, n):     # v에서 w로 갈 수 있고, w가 아직 방문 X면
                if computers[v][w] == 1 and visited[w] == 0:
                    q.append(w)       # 큐에 추가하고,
                    visited[w] = cnt  # 방문 처리(몇 번재 네트워크인지 처리)
        cnt += 1               # bfs가 끝나면 한 네트워크가 끝난거니까 다음 네트워크로 (+1)
    
    for i in range(n):         # 모든 컴퓨터에 대해서 반복해야함
        if not visited[i]:     # 모든 컴퓨터를 다 방문처리할 때까지 
            bfs(i)
            
    return max(visited)