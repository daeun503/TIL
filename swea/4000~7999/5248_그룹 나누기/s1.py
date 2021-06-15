import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

def bfs(s):
    global cnt
    cnt += 1

    q = [s]
    visited[s] = 1
    while q:
        v = q.pop(0)
        for w in range(1, N+1):
            if G[v][w] and not visited[w]:
                q.append(w)
                visited[w] = 1

def dfs(s):
    global cnt
    cnt += 1

    stack = [s]
    visited[s] = 1
    while stack:
        v = stack.pop()
        for w in range(1, N+1):
            if G[v][w] and not visited[w]:
                q.append(w)
                visited[w] = 1


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    IN = list(map(int, input().split()))

    # 인접 행렬
    G = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        G[IN[2*i]][IN[2*i+1]] = 1
        G[IN[2*i+1]][IN[2*i]] = 1

    visited = [0]*(N+1)

    cnt = 0
    for j in range(1, N+1):
        if not visited[j]:
            bfs(j)

    print("#{} {}".format(tc, cnt))