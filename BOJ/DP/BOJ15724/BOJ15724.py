import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        # (i, j) 값은 왼쪽(i, j-1) + 위쪽 (i-1, j) - 11시 대각선 (i-1, j-1) + 해당 영역 값
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + IN[i-1][j-1]

# dp 값으로부터 주어진 좌표 사이 값을 구함
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(ans)
