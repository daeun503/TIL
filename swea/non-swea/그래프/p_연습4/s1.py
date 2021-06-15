"""
연습 문제4. bfs 구현
 - bfs 방식으로 그래프를 탐색하시오.
"""

def bfs(s):
    q = [s]
    visited[s] = 1
    while q:
        v = q.pop(0)
        print(v, '방문')
        for w in range(V+1):
            if G[v][w] and not visited[w]:
                q.append(w)
                visited[w] = 1

def bfs_distance(s):
    q = [s]
    visited[s] = 0
    while q:
        v = q.pop(0)
        print('{}에 방문 {}로부터 거리는 {}'.format(v, s, visited[v]))
        for w in range(V+1):
            if G[v][w] and visited[w] == -1:
                q.append(w)
                visited[w] = 1 + visited[v]


import sys
sys.stdin = open('input.txt')

# 정점, 간선 정보 초기화
V, E = map(int, input().split())

# 그래프, 방문 정보 초기화
IN = list(map(int, input().split()))
visited = [0] * (V+1)

# 그래프 그리기
G = [[0]*(V+1) for _ in range(V+1)]
for i in range(0, len(IN), 2):
    G[IN[i]][IN[i+1]] = 1
    G[IN[i+1]][IN[i]] = 1

# 탐색 시작
bfs(1)

print('---------------')
visited = [-1] * (V+1)

# 시작 정점으로부터의 거리(visited 활용)
bfs_distance(1)

