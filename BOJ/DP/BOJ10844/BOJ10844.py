import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

N = int(input())
DP = [[0] * 10 for _ in range(N+1)]

# x축: 0__, 1__, 2__ ... => x로 시작하는 계단 수
# y축: 숫자 길이
for i in range(10):
    DP[1][i] = 1

for r in range(2, N+1):
    for c in range(10):
        tmp1 = (c-1 >= 0) and DP[r-1][c-1]
        tmp2 = (c+1 < 10) and DP[r-1][c+1]
        # 11시, 1시 방향에 위치한 두 값을 더해준다.
        DP[r][c] = (tmp1 + tmp2) % 1000000000

# DP[N][0]은 0으로 시작하는 계단 수는 불가능하므로 빼준다
print(sum(DP[N][1:]) % 1000000000)
