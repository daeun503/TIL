import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * M for _ in range(N)]
for r in range(N):
    for c in range(M):
        result[r][c] = matrix[r][c] + \
                        (r > 0 and result[r-1][c]) + (c > 0 and result[r][c-1]) - \
                        (r > 0 and c > 0 and result[r-1][c-1])

ans = -9999999999999
for x1 in range(N):
    for y1 in range(M):
        for x2 in range(x1, N):
            for y2 in range(y1, M):
                tmp = result[x2][y2] - \
                      (y1 > 0 and result[x2][y1-1]) - (x1 > 0 and result[x1-1][y2]) + \
                      (x1 > 0 and y1 > 0 and result[x1-1][y1 - 1])
                ans = max(ans, tmp)
print(ans)
