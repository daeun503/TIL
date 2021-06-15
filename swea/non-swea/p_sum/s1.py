import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for i in range(100)]

    result_max = 0
    tmp_row, tmp_col, tmp_rl, tmp_lr = 0, 0, 0, 0

    for i in range(len(matrix)):
        # row 방향, col 방향 한 줄 합, 최대값 구하기
        tmp_row, tmp_col = 0, 0
        for j in range(len(matrix[0])):
            tmp_row += matrix[i][j]
            tmp_col += matrix[j][i]
        if tmp_row >= result_max: result_max = tmp_row
        if tmp_col >= result_max: result_max = tmp_col

    # rl(\) 방향 lr(/)방향 합, 최대값 구하기
        tmp_rl += matrix[i][i]
        tmp_lr += matrix[99-i][i]
    if tmp_rl >= result_max: result_max = tmp_rl
    if tmp_lr >= result_max: result_max = tmp_lr

    print("#{} {}".format(tc, result_max))
