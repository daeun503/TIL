import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    IN = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(len(IN[0])):
            if IN[r][c] == "A":
                for i in range(4):
                    for j in range(1, 2):
                        check_r = r + dr[i] * j
                        check_c = c + dc[i] * j
                        if 0 <= check_r < N and 0 <= check_c < len(IN[0]):
                            IN[check_r][check_c] = 'X'

            elif IN[r][c] == "B":
                for i in range(4):
                    for j in range(1, 3):
                        check_r = r + dr[i] * j
                        check_c = c + dc[i] * j
                        if 0 <= check_r < N and 0 <= check_c < len(IN[0]):
                            IN[check_r][check_c] = 'X'

            elif IN[r][c] == "C":
                for i in range(4):
                    for j in range(1, 4):
                        check_r = r + dr[i] * j
                        check_c = c + dc[i] * j
                        if 0 <= check_r < N and 0 <= check_c < len(IN[0]):
                            IN[check_r][check_c] = 'X'
    # 출력
    result = 0
    for i in IN:
        result += i.count('H')
    print(result)

    print(DataFrame(IN))
