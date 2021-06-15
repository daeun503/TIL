import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

T = int(input())
for tc in range(1, T+1):
    result = 1
    want = sum([1, 2, 3, 4, 5, 6, 7, 8, 9])

    # 행 검사
    problem = [list(map(int, input().split())) for _ in range(9)]
    for row in problem:
        if sum(row) != want:
            result = 0

    # 열 검사
    problem_col = [list(i) for i in zip(*problem)]
    for column in problem_col:
        if sum(column) != want:
            result = 0

    # 9칸 검사
    for k in range(0, 7, 3):
        for l in range(0, 7, 3):
            tmp = 0
            for x in range(3):
                for y in range(3):
                    tmp += problem[k+x][l+y]
            if tmp != want:
                result = 0

    print("#{} {}".format(tc, result))

