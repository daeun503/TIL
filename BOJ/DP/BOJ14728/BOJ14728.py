import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

"""
방법 1

N, T = map(int, input().split())
K, S = [0], [0]
for _ in range(N):
    k, s = map(int, input().split())
    K.append(k)
    S.append(s)

dp = [[0] * (T+1) for _ in range(N+1)]
for i in range(1, N+1):
    weight, value = K[i], S[i]
    for j in range(1, T+1):
        # 가용 무게가 더 크면 선택(왼쪽)하거나 선택X(위쪽)
        if j >= weight:
            dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])
        # 가용 무게가 더 작으면 선택할 수 없다
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][T])
"""

N, T = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (T+1)
for weight, value in IN:
    for j in range(T, weight-1, -1):
        dp[j] = max(dp[j], dp[j-weight] + value)
print(dp[T])
