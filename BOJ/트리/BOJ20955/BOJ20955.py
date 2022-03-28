import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque


def bfs(n):
    q = deque([n])
    visited[n] = 1
    edge = 0
    while q:
        v = q.popleft()
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1
                edge += 1
    return edge


N, M = map(int, input().split())
visited = [0] * (N+1)
G = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[v].append(u)
    G[u].append(v)

result = 0
for n in range(1, N+1):
    if not visited[n]:
        # 트리 덩어리를 이어준다
        result += 1
        # 필요없는 간선을 끊어준다. 필요없는 간선 => (모든 간선 - 필요한 간선)
        # 여기서 빼주는건 "필요한 간선". print할 때 "모든 간선"을 더해줌
        result -= bfs(n)

print(result + M - 1)
