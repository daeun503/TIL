import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


def my_func(current, charge, current_E):
    global result

    # 종료 조건
    if current == N:
        if result > charge:
            result = charge
        return

    # 유망성검사
    if result <= charge:
        return

    # 백트래킹1: 충전 하고 가기
    my_func(current+1, charge+1, E[current]-1)
    # 백트래킹2: 충전 안하고 가기
    if current_E >= 1:
        my_func(current+1, charge, current_E-1)


for tc in range(1, int(input())+1):
    E = list(map(int, input().split()))
    N = E[0]
    result = 999999
    # E 1 깎고 위치 2부터 시작
    my_func(2, 0, E[1]-1)
    print("#{} {}".format(tc, result))








