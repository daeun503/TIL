import sys

from pandas import DataFrame
sys.stdin = open('input.txt')


for tc in range(1, int(input())+1):
    N = int(input())
    IN = [[-99]*(N+2)] + [[-99] + list(map(int, input().split())) + [-99] for _ in range(N)] + [[-99]*(N+2)]
    DP = [[-99]*(N+2)] + [[-99] + [0]*N  + [-99] for _ in range(N)] + [[-99]*(N+2)]
    visited = [0] * (N*N+1)

    k = 0
    for r in range(1, N+1):
        for c in range(1, N+1):
            k += 1
            if IN[r][c]+1 in [IN[r+1][c], IN[r-1][c], IN[r][c+1], IN[r][c-1]]:
                visited[IN[r][c]] = 1

    max_move, move, room = 0, 0, 0
    i = 0
    while i < len(visited):
        if visited[i]:
            move = 1
            for j in range(i, len(visited)):
                if visited[j] == 1:
                    move += 1
                else:
                    if move > max_move:
                        max_move = move
                        room = i
                    i = j
                    break
        i += 1

    print("#{} {} {}".format(tc, room, max_move))