import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

for tc in range(1, int(input())+1):
    N = float(input())
    result = ''
    for i in range(1, 13):
        if N == 0: break     # N이 2진수로 바꼈으면 끝
        if N >= 2**(-i):     # N이 2^(-i)보다 크면
            result += '1'    # 해당 자리에 1넣을 수 있음
            N -= 2 ** (-i)   # 그 만큼 N에서 빼주고 만복
        else:
            result += '0'    # 작으면 해당 자리에 못 넣음

    result = 'overflow' if N else result
    print('#{} {}'.format(tc, result))