import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)
for i in range(N):
    # i+T[i]일의 최대 값은 i일까지 최대 값 + i일에서 상담 값
    if i + T[i] <= N:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])
    # i일이랑 i+1일이랑 비교해서, i+1일이 값 더 작으면 i일 최대값으로 갱신
    dp[i + 1] = max(dp[i], dp[i + 1])

print(dp[N])
