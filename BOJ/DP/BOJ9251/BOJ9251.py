import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

s1 = input()
s2 = input()

N = len(s1)
M = len(s2)

dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        # 일치할 경우 왼쪽 대각선(i-1, j-1) 로부터 + 1
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # 불일치할 경우 왼쪽(i, j-1)이나 위(i-1, j)로부터 max값
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][M])
