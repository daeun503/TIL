import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, int(input())+1):
    N = int(input())
    IN = [list(map(int, list(input()))) for _ in range(N)]
    result = 0

    for r in range(N):
        for c in range(N):
            if IN[r][c] == 2: s = (r, c)

    # 초기값, 초기 방문표시
    stack = [s]
    IN[s[0]][s[1]] = 1

    while stack:
        r, c = stack.pop()
        cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # nr, nc가 범위 내이면
            if 0 <= nr < N and 0 <= nc < N:
                # 갈 수 있는 길이면 nr, nc를 스택에 넣고 방문표시
                if IN[nr][nc] == 0:
                    stack.append((nr, nc))
                    IN[nr][nc] = 1
                # 도착지면 result에 1 넣고 끝내기
                elif IN[nr][nc] == 3:
                    result = 1

        if result : break
    print("#{} {}".format(tc, result))