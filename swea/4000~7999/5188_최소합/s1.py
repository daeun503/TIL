import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


# DP 버전
for tc in range(1, int(input())+1):
    N = int(input())
    IN = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if r == 0 and c == 0:
                continue
            elif r == 0:
                IN[r][c] = IN[r][c-1]+IN[r][c]
            elif c == 0:
                IN[r][c] = IN[r-1][c] + IN[r][c]
            else:
                IN[r][c] = min(IN[r-1][c]+IN[r][c], IN[r][c-1]+IN[r][c])

    print("#{} {}".format(tc, IN[N-1][N-1]))

############################################################################

# 백트래킹 버전
def my_func(route, my_sum):
    global result

    # 종료 조건 : 마지막 위치에 도달했을 때
    if route[-1] == (N-1, N-1):
        if result > my_sum:
            result = my_sum
            # print(route)
        return

    # 유망성 검사 : my_sum이 저장한 result보다 커지면 유망 X
    if result < my_sum:
        return

    # 백트래킹
    r, c = route[-1]
    if r == N-1:     # 맨 아랫줄이면 오른쪽으로만 이동
        my_func(route+[(r, c+1)], my_sum + IN[r][c+1])  # 오른쪽
    elif c == N-1:   # 맨 오른쪽 줄이면 아래로만 이동
        my_func(route+[(r+1, c)], my_sum + IN[r+1][c])  # 아래
    else:            # 중간이면 오른쪽, 아래 둘 다 이동해보기
        my_func(route+[(r, c+1)], my_sum + IN[r][c+1])  # 오른쪽
        my_func(route+[(r+1, c)], my_sum + IN[r+1][c])  # 아래

for tc in range(1, int(input())+1):
    N = int(input())
    IN = [list(map(int, input().split())) for _ in range(N)]
    result = 999999
    my_func([(0, 0)], IN[0][0])
    print("#{} {}".format(tc, result))
