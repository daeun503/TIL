import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

# 정점, 간선의 개수
N, M = map(int, input().split())
node = list(map(int, input().split()))

# 인접 행렬 생성
G = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(0, len(node), 2):
    G[node[i]][node[i+1]] = 1
    G[node[i+1]][node[i]] = 1
print(DataFrame(G))

# DFS 탐색
visited = [0] * (N+1)
stack = []

def DFS(v):
    stack.append(v)
    visited[v] = 1

    while stack:
        v = stack.pop()
        for w in range(1, N+1):
            if G[v][w] == 1 and visited[w] == 0:
                stack.append(w)
                visited[w] = 1

DFS(1)