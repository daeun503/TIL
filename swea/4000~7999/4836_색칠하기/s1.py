import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

T = int(input())

for tc in range(1, T+1):
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())

    # 컬러 색칠하기
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                matrix[r][c] = color if matrix[r][c] == color else matrix[r][c] + color

    cnt = 0
    for i in matrix:
        for j in i:
            if j == 3:
                cnt += 1

    # print(DataFrame(matrix))
    print("#{} {}".format(tc, cnt))
