import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

# 오른쪽 아래 왼쪽 위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def serch(x, y):
    k = 2
    r, c = x-1, y-1
    result = []
    flag = 1

    while flag:
        for i in range(4):
            for _ in range(k):
                nr = dr[i] + r
                nc = dc[i] + c
                if 0<=nr<N and 0<=nc<N:
                    r, c = nr, nc
                    if IN[r][c] == 2:
                        result.append([r, c])
                        flag = 0
        k += 2

    for i in range(len(result)):
        result[i].append(abs(result[i][0]-x)+abs(result[i][1]-y))
    result.sort(key = lambda f: f[2])
    return result[0]



for tc in range(1, 10):
    N, M = map(int, input().split())
    IN = [list(map(int, input().split())) for _ in range(N)]
    print(DataFrame(IN))

    for r in range(N):
        for c in range(N):
            if IN[r][c]:
                cr, cc, cd = serch(r, c)
                IN[cr][cc] += 1



