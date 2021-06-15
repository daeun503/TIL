import sys
sys.stdin = open("input2.txt", "r")
# 연습 문제 1

T = int(input())
N = int(input())

for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # r: 행,  c: 열
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

# 1. 가장 자리 제외
    total = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            r, c = i, j
            result = 0
            for k in range(4):
                result += abs(matrix[r+dr[k]][c+dc[k]] - matrix[r][c])
            total.append(result)
    print("가장 자리 제외:", sum(total))

#2. 가장 자리를 포함하여 계산
    total = []
    for i in range(0, N):
        for j in range(0, N):
            r, c = i, j
            result = 0
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    result += 0
                else:
                    result += abs(matrix[nr][nc] - matrix[r][c])
            total.append(result)
    print("가장 자리 포함:", sum(total))
