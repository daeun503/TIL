import sys

sys.stdin = open("input.txt", "r")


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 100%에서 틀렸다면 M=1인 경우
if M == 1:
    for r in range(N):
        print(*map(lambda x: -x, matrix[r]))
    exit()

# M이 1 이상인 경우
result = [[0] * N for _ in range(N)]
result_DP = [[0] * N for _ in range(N)]

center = M // 2
for r in range(N):
    for c in range(N):
        # 테두리 부분은 0 으로 만들어주기
        if (
            0 <= r < center
            or 0 <= c < center
            or N - center <= r < N
            or N - center <= c < N
        ):
            result[r][c] = 0
            continue

        target_r, target_c = r - center, c - center

        # M 넓이의 땅에 매설된 폭탄 양 => result_DP[r][c]에 대해 정리
        # bomb = result_DP[r][c] - result_DP[r - M][c] - result_DP[r][c - M] + result_DP[r - M][c - M]
        bomb = -matrix[target_r][target_c]
        if 0 <= r - M < N:
            bomb += result_DP[r - M][c]
        if 0 <= c - M < N:
            bomb += result_DP[r][c - M]
        if 0 <= r - M < N and 0 <= c - M < N:
            bomb -= result_DP[r - M][c - M]
        result_DP[r][c] = bomb

        # result_DP로 result 값 구하기
        result[r][c] = (
            result_DP[r][c]
            - result_DP[r - 1][c]
            - result_DP[r][c - 1]
            + result_DP[r - 1][c - 1]
        )

for r in range(N):
    print(*result[r])
