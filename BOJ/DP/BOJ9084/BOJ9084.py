import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

for _ in range(int(input())):
    N = int(input())
    IN = [list(map(int, input().split())) for _ in range(2)]

    # N이 2이하일 때 예외처리
    if N == 1:
        print(max(IN[0][0], IN[1][0]))
        continue
    elif N == 2:
        print(max(IN[0][0] + IN[1][1], IN[1][0] + IN[0][1]))
        continue

    # N이 3이상일 때 DP
    IN[0].extend([0, 0])
    IN[1].extend([0, 0])

    # DP 초기화
    DP = [[0]*(N+2) for _ in range(2)]
    DP[0][0], DP[0][1], DP[1][0], DP[1][1] = IN[0][0], IN[0][1], IN[1][0], IN[1][1]

    for i in range(N):
        # 0행에서 시작한 DP (=> DP[0][i] 출발)
        DP[1][i+1] = max(DP[1][i+1], DP[0][i] + IN[1][i+1])
        DP[0][i+2] = max(DP[0][i+2], DP[0][i] + IN[1][i+1] + IN[0][i+2])
        DP[1][i+2] = max(DP[1][i+2], DP[0][i] + IN[1][i+2])

        # 1행에서 시작한 DP (=> DP[1][i] 출발)
        DP[0][i+1] = max(DP[0][i+1], DP[1][i] + IN[0][i+1])
        DP[1][i+2] = max(DP[1][i+2], DP[1][i] + IN[0][i+1] + IN[1][i+2])
        DP[0][i+2] = max(DP[0][i+2], DP[1][i] + IN[0][i+2])

    print(max(DP[0][N-2], DP[0][N-1], DP[1][N-2], DP[1][N-1]))


