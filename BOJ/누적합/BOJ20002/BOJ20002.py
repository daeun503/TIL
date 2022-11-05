import sys
from pandas import DataFrame

sys.stdin = open("input.txt", "r")

N = int(input())
IN = [list(map(int, input().split())) for _ in range(N)]

# IN에 대한 누적합 배열 DP 만들기
DP = [[0] * (N + 1) for _ in range(N + 1)]
max_result = IN[0][0]    # 크기 1짜리 max값 미리 구해놓기
for r in range(1, N + 1):
    for c in range(1, N + 1):
        DP[r][c] = IN[r - 1][c - 1] + DP[r - 1][c] + DP[r][c - 1] - DP[r - 1][c - 1]
        max_result = max(max_result, IN[r - 1][c - 1])


# 누적합 배열 DP로부터 특정 K x K 영역의 합 구하기, K는 2이상임
# (r, c) 기준으로 k만큼의 넓이를 구함
for r in range(1, N + 1):
    for c in range(1, N+1):
        for k in range(1, min(r, c) + 1):
            value = DP[r][c] - DP[r - k][c] - DP[r][c - k] + DP[r - k][c - k]
            max_result = max(max_result, value)

print(max_result)
