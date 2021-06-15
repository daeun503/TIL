import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 위, 아래, 왼쪽, 오른쪽
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def my_func(x, y, route):
    global result

    # 길이가 7이 되면 추가
    if len(route) == 7:
        result.add(route)
        return

    # 4방으로 탐색
    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            my_func(nr, nc, route+str(IN[nr][nc]))


for tc in range(1, int(input()) + 1):
    IN = [list(map(int, input().split())) for _ in range(4)]

    result = set()
    # 임의의 위치에서 시작이니까 모든 격자판에서 시작
    for x in range(4):
        for y in range(4):
            my_func(x, y, str(IN[x][y]))

    print("#{} {}".format(tc, len(result)))