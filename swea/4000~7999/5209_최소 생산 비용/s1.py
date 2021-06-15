import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

# 배열 최소합과 똑같
def my_func(pick, my_sum):
    global result
    r = len(pick)

    # 종료 조건
    if r == N:
        if result > my_sum:
            result = my_sum
        return

    # 유망성
    if result < my_sum:
        return

    # 백트래킹
    for c in range(N):
        if c not in pick:
            my_func(pick+[c], my_sum+IN[r][c])

for tc in range(1, int(input())+1):
    N = int(input())
    IN = [list(map(int, input().split())) for _ in range(N)]
    result = 999999
    my_func([], 0)
    print("#{} {}".format(tc, result))