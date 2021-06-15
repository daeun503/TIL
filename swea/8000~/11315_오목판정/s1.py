import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 상하좌우 // 대각선
dr = [-1, 1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, -1, 1, 1, -1, -1, 1]


def my_func(IN):
    for r in range(len(IN)):
        for c in range(len(IN[0])):
            if IN[r][c] == 'o':
                # 8방향 탐색
                for i in range(8):
                    check = 1
                    for j in range(1, 5):
                        check_r = r + dr[i] * j
                        check_c = c + dc[i] * j
                        if 0 <= check_r < N and 0 <=  check_c < N and IN[check_r][check_c] == 'o':
                            check += 1
                        else:
                            break
                    if check == 5:
                        return 1
    return 0

def my_func2(N, IN):
    for r in range(N):
        for c in range(N):
            if IN[r][c] == 'o':
                for i in range(8):
                    check = 1
                    check_r = r + dr[i]
                    check_c = c + dc[i]
                    while 0 <= check_r < N and 0 <=  check_c < N and IN[check_r][check_c] == 'o':
                        check += 1
                        check_r += dr[i]
                        check_c += dc[i]
                        if check == 5:
                            break
                    if check == 5:
                        return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    IN = [list(input()) for _ in range(N)]

    # result = "YES" if my_func(IN) else "NO"
    result = "YES" if my_func2(N, IN) else "NO"
    print("#{} {}".format(tc, result))



