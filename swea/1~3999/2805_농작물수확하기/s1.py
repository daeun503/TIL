import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, map(str, input()))) for _ in range(N)]

    center = N // 2
    i, r, result = 0, 0, 0

    # 위쪽 절반
    while r != N//2:
        for c in range(center-i, center+i+1):
            result += matrix[r][c]
        i += 1
        r += 1

    # 아래쪽 절반
    while r != N:
        for c in range(center-i, center+i+1):
            result += matrix[r][c]
        i -= 1
        r += 1

    print("#{} {}".format(tc, result))