import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

N, K = map(int, input().split())
IN = [[0, 0]]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    IN.append(list(map(int, input().split())))

# 냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = IN[i][0]
        value = IN[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]  # weight보다 작으면 위의 값을 그대로 가져온다
        else:
            dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i - 1][j])

print(dp[N][K])
