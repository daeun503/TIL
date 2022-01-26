import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

N = int(input())
W = [0] + list(map(int, input().split()))
V = [0] + list(map(int, input().split()))

dp = [[0]*100 for _ in range(N+1)]

for i in range(1, N+1):
    weight, value = W[i], V[i]
    for j in range(1, 100):
        if j >= weight:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][99])
