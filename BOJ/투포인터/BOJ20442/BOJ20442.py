import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# https://ws-pace.tistory.com/108 참고

IN = input()
N = len(IN)
result = IN.count("R")
if not result:
    print(0)
    exit()

# LK => 인덱스 기준 왼쪽에 있는 K의 개수
LK, tmp = [0] * N, 0
for i in range(N-1):
    if IN[i] == "K":
        tmp += 1
    LK[i+1] = tmp

# RK => 인덱스 기준 오른쪽에 있는 K의 개수
RK, tmp = [0] * N, 0
for j in range(N-1, 0, -1):
    if IN[j] == "K":
        tmp += 1
    RK[j-1] = tmp

s, e = 0, N - 1
while s <= e:
    # s, e가 가리키는 값이 K이면 패스
    if IN[s] == "K":
        s += 1
    elif IN[e] == "K":
        e -= 1
    # s, e가 가리키는 값이 R일 때
    else:
        # IN[s:e+1].count("R") 하니까 시간 초과
        # s, e 사이의 R 개수 + 양 쪽 K의 개수
        current = - s - RK[s] + e + RK[e] + 1 + min(LK[s], RK[e]) * 2
        result = max(result, current)
        # LK가 더 크면 왼쪽에 K가 많으니까, 오른쪽을 늘려야 함 e - 1
        if LK[s] > RK[e]:
            e -= 1
        # RK가 더 크면 오른쪽에 K가 많으니까 왼쪽을 늘려야 함 s + 1
        else:
            s += 1

print(result)
