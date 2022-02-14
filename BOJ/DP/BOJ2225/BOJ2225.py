import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

N, K = map(int, input().split())

DP = [[0] * (N+1) for _ in range(K+1)]
# 0행: 0개의 수로 n의 값 만들기 => 모두 0
# 1행: 1개의 수로 n의 값 만들기 => 모두 1
for i in range(N+1):
    DP[1][i] = 1
# 0열: k개의 수로 0의 값 만들기 => 모두 1 (0, 0, 0...)
for j in range(K+1):
    DP[j][0] = 1

# DP 테이블 채우기
for r in range(2, K+1):
    for c in range(1, N+1):
        DP[r][c] = (DP[r][c - 1] + DP[r - 1][c]) % 1000000000

print(DP[K][N])
