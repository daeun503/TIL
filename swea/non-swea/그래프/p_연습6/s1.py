"""
연습 문제6.
채점 완료 후 해당 화면을 캡처하여 폴더에 첨부하여 업로드 해주세요!

 - BOJ 2583 영역 구하기
 - 그래프 탐색의 가벼운 응용 버전
"""

import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(s):
    matrix[s[0]][s[1]] = 1
    q = [s]
    result = 1
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < M and 0 <= nc < N:
                if matrix[nr][nc] == 0:
                    q.append((nr, nc))
                    matrix[nr][nc] = matrix[r][c] + 1
                    result += 1
    return result

M, N, K = map(int, input().split())
matrix = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            matrix[r][c] = -1

result = []
result_n = 0
for r in range(M):
    for c in range(N):
        if matrix[r][c] == 0:
            result.append(bfs((r, c)))
            result_n += 1

print(result_n)
print(*sorted(result))
