import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # # *과 zip을 활용한 전치 행렬 참고
    # matrix = [list(map(int, input().split())) for _ in range(9)]
    # matrix_trans = [list(i) for i in zip(*matrix)]

    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix90 = [list(i)[::-1] for i in zip(*matrix)]
    matrix180 = [list(i)[::-1] for i in zip(*matrix90)]
    matrix270 = [list(i)[::-1] for i in zip(*matrix180)]



    print("#{}".format(tc))
    for i in range(N):
        print(''.join(map(str, matrix90[i])), ''.join(map(str, matrix180[i])), ''.join(map(str, matrix270[i])))