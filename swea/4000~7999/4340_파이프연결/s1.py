import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


def next(next_PIPE, r, c, connect):
    next_connect = PIPE[next_PIPE].strip(connect)
    if next_connect == 'a':
        nr, nc = r-1, c
    elif next_connect == 'b':
        nr, nc = r, c+1
    elif next_connect == 'c':
        nr, nc = r+1, c
    else:
        nr, nc = r, c-1
    return (nr, nc, next_connect)

for tc in range(1, int(input()) + 1):
    N = int(input())
    IN = [list(map(int, input().split())) for _ in range(N)]

    PIPE = {0: [], 1: 'bd', 2: 'ac', 3: 'bc', 4: 'cd', 5: 'ad', 6: 'ab',}
    connect_nextPIPE = {'a': [2, 5, 6], 'b': [1, 3, 6], 'c': [2, 3, 4], 'd': [1, 4, 5]}

    BP = [[0]*N for _ in range(N)]

    q = [(0, 0, 'b')]
    BP[0][0] = 1
    while q:
        r, c, connect = q.pop(0)
        for num in connect_nextPIPE[connect]:
            nr, nc, next_connect = next(num, r, c, connect)
            if 0 <= nr < N and 0 <= nc < N:
                if BP[nr][nc] == 0 or BP[nr][nc] > BP[r][c] + 1:
                    BP[nr][nc] = BP[r][c] + 1
                    q.append((nr, nc, next_connect))



    print(DataFrame(IN))
    print()
    print(DataFrame(BP))

    print()
    print("#{} {}".format(tc, BP[N-1][N-1]))

