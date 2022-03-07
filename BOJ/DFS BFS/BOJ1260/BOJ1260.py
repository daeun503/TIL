import sys
sys.stdin = open("input.txt", "r")


def bfs(start):
    visited = [0] * (N+1)
    visited[start] = 1
    result = []
    q = [start]
    while q:
        v = q.pop(0)
        result.append(v)
        for w in range(1, N+1):
            if G[v][w] and not visited[w]:
                q.append(w)
                visited[w] = 1
    return result


def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    for w in range(1, N+1):
        if G[v][w] and not visited[w]:
            dfs(w)


N, M, V = map(int, input().split())
G = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    v, w = map(int, input().split())
    G[v][w] = 1
    G[w][v] = 1

visited = [0] * (N+1)
dfs(V)
print()
print(*bfs(V))
