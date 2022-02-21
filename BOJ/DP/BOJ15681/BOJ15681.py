import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def go(r):
    # 본인 포함이라 1부터 시작
    count = 1
    # 방문 체크
    close[r] = 1
    # 연결된 노드들에 대해 탐색
    for v in G[r]:
        # 이미 방문 했으면(=부모 노드) 패스 / 방문하지 않았으면 방문
        if not close[v]:
            close[v] = 1
            count += dp[v] if dp[v] else go(v)
    # dp 값 갱신
    dp[r] = count
    return count


N, R, Q = map(int, input().split())

G = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

dp = [0] * (N+1)
close = [0] * (N+1)
go(R)
for _ in range(Q):
    u = int(input())
    print(dp[u])
