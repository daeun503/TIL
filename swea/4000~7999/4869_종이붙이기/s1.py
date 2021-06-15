import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

T = int(input())

def my_func(N):
    # 10 ~ 20 하드코딩
    if N == 10:
        return 1
    elif N == 20:
        return 3
    # 10이 최소 하나 끼어 있을 때 (30, 50...)
    elif N % 20:
        return my_func(N - 20) * 2 * 2 + 1
    # 10이 안 끼어 있어도 될 때 (40, 60...)
    else:
        return my_func(N - 20) * 2 * 2 - 1

for tc in range(1, T+1):
    N = int(input())
    result = my_func(N)
    print("#{} {}".format(tc, result))