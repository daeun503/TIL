import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


def my_func(matrix):
    result = 0
    for r in range(len(matrix)-1):
        for c in range(len(matrix[0])-1):
            if not (matrix[r][c] or matrix[r+1][c] or matrix[r][c+1] or matrix[r+1][c+1]):
                result += 1
                matrix[r][c] = 1
                matrix[r + 1][c] = 1
                matrix[r][c + 1] = 1
                matrix[r + 1][c + 1] = 1
    return result

# 오른쪽 아래 왼쪽 위
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def my_func2(matrix):
    r, c, = 0, -1
    dir = 0
    num = 1
    result = 0
    while num < min(len(matrix), len(matrix[0]))//2 :
        for dr, dc in [drc[dir]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < H-1 and 0 <= nc < W-1:
                r, c = nr, nc
                if not (matrix[r][c] or matrix[r + 1][c] or matrix[r][c + 1] or matrix[r + 1][c + 1]):
                    result += 1
                    matrix[r][c] = 1
                    matrix[r + 1][c] = 1
                    matrix[r][c + 1] = 1
                    matrix[r + 1][c + 1] = 1
            else:
                dir = (dir + 1) % 4
                if dir == 0:
                    num += 1
                    r += 1
                    c += 1
    return result


for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    matrix1 = [list(map(int, input().split())) for _ in range(H)]
    matrix2 = [list(i) for i in zip(*matrix1[::-1])]
    matrix3 = [list(i) for i in zip(*matrix2[::-1])]
    matrix4 = [list(i) for i in zip(*matrix3[::-1])]
    matrix5 = [list(i) for i in zip(*matrix4[::-1])]

    result1 = my_func(matrix1)
    result2 = my_func(matrix2)
    result3 = my_func(matrix3)
    result4 = my_func(matrix4)
    result5 = my_func2(matrix5)

    print(max(result1, result2, result3, result4, result5))
    print(result5)
    print()
