import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

N = int(input())
IN = [int(input()) for i in range(N)]

if N == 1:
    print(IN[0])
    exit()
elif N == 2:
    print(IN[0] + IN[1])
    exit()

dp = [0] * N
dp[0] = IN[0]
dp[1] = IN[0] + IN[1]
# 이 부분 마지막 항 안 써서 틀림
dp[2] = max(IN[0]+IN[1], IN[1]+IN[2], IN[0]+IN[2])

for n in range(N-3):
    dp[n+3] = max(dp[n] + IN[n+2] + IN[n+3], dp[n+1] + IN[n+3], dp[n+2])

print(dp[N-1])
