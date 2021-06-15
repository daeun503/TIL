import sys
sys.stdin = open('input.txt')

# r: 행,  c: 열 / 상하좌우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0 for col in range(N)] for row in range(N)]

    # r, c: 좌표 . row: 테두리 길이 . tmp: 이전 테두리까지 합
    r, c, tmp, row = 0, 0, 0, N

    # 숫자 1부터 N^2까지 입력할 예정
    for i in range(1, N**2+1):
        matrix[r][c] = i

        # 만약, 테두리 한 줄을 다 채웠으면 오른쪽으로 이동하고 row는 -2
        # row길이의 테두리 한 줄 : row + 2*(row-1) + (row-2)
        if i == tmp + row + 2*(row-1) + (row-2):
            nr, nc = 0, 1
            row -= 2
            tmp += i

        if r + c == N - 1 and r > c:      # 하단 왼쪽 모서리 -> 위로 이동
            nr, nc = -1, 0
        elif r + c == N - 1 and r < c:    # 상단 오른쪽 모서리 -> 아래로 이동
            nr, nc = 1, 0
        elif r == c and r >= N // 2:      # 하단 오른쪽 모서리 -> 왼쪽 이동
            nr, nc = 0, -1
        elif r == c and r < N // 2:       # 상단 왼쪽 모서리 -> 오른쪽 이동
            nr, nc = 0, 1

        r += nr
        c += nc

    print("#{}".format(tc))
    for m in matrix: print(*m)