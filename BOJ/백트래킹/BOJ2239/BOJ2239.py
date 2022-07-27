import sys
sys.stdin = open("input.txt", "r")


def check(r, c, value):
    # 가로 줄에 value가 있는지 확인
    if value in IN[r]:
        return False
    # 세로 줄에 value가 있는지 확인
    if value in map(lambda x: x[c], IN):
        return False
    # 3x3 정사각형에 value가 있는지 확인
    unit_r, unit_c = 3 * (r // 3), 3 * (c // 3)
    for i in range(unit_r, unit_r + 3):
        for j in range(unit_c, unit_c + 3):
            if value == IN[i][j]:
                return False
    return True


def func(num):
    # 마지막 칸이면 답 출력하고 종료
    if num == 81:
        for r in range(9):
            print(''.join(map(str, IN[r])))
        exit()

    r, c = num // 9, num % 9
    # 숫자가 채워져 있으면 넘어가기
    if IN[r][c]:
        func(num + 1)
    # 숫자가 채워져 있지 않으면
    else:
        for n in range(1, 10):
            # 숫자 n이 유효한지 확인해서 유효하면 숫자 입력
            if check(r, c, n):
                IN[r][c] = n
                func(num + 1)
                IN[r][c] = 0

IN = [list(map(int, list(input()))) for _ in range(9)]
func(0)
