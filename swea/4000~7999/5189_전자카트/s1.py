import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


def my_func(route, my_sum, r):
    global result

    # 종료 조건: 한 사이클 다 돌고 사무실로 돌아왔을 때
    if len(route) == N+1:
        if route[-1] == 0 and result > my_sum:
            result = my_sum
            # print(route)
        return

    # 유망성 검사: 현재 루트가 미리 계산한 최솟값보다 작으면 유망X
    if result < my_sum:
        return

    # 백트래킹
    for c in range(N):
        if visited[c] == 0:
            visited[c] = 1
            my_func(route+[c], my_sum+IN[r][c], c)
            visited[c] = 0


MAX = 999999
for tc in range(1, int(input())+1):
    N = int(input())
    IN = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        IN[i][i] = MAX
    result = MAX
    visited = [0] * N
    my_func([0], 0, 0)

    print("#{} {}".format(tc, result))