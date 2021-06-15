import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

# 평소에 하던 방식. 이것도 통과하긴 하는데 방문 체크로 하는 것보다 오래 걸린다. (12,798 ms)
# in이나 pick+[c] 에서 시간이 오래 걸리는 듯? pick는 짧은 것 같은데 횟수가 많으니 오래 걸리나보다..
def my_func(pick, P):
    global result
    r = len(pick)

    # 종료 조건
    if r == N:
        if result < P:
            result = P
        return

    # 유망성 (확률 더 곱해봤자 작아지기만 함)
    if result >= P:
        return

    # 백트래킹
    for c in range(N):
        if c not in pick:
            my_func(pick + [c], P * IN[r][c])


# 방문 체크로 (4,592 ms)
def my_func2(r, P):
    global result

    # 종료 조건
    if r == N:
        if result < P:
            result = P
        return

    # 유망성 (확률 더 곱해봤자 작아지기만 함)
    if result >= P:
        return

    # 백트래킹
    for c in range(N):
        if visited[c] == 0:
            visited[c] = 1
            my_func(r+1, P * IN[r][c])
            visited[c] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    IN = [list(map(lambda x: int(x) * 0.01, input().split())) for _ in range(N)]
    result = 0
    my_func([], 1)
    visited = [0] * N
    # my_func2(0, 1)
    print("#{} {:.6f}".format(tc, result * 100))
