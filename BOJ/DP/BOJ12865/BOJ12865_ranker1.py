import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

N, K = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K+1)
for weight, val in ary:
    for j in range(K, weight-1, -1):
        dp[j] = max(dp[j], dp[j-weight] + val)

print(dp[K])
