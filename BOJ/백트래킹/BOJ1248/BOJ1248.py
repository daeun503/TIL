# import sys
# sys.stdin = open("input.txt", "r")

# arr의 마지막 idx (check_idx) 값이 적절한지 확인
def check(arr):
    check_idx = len(arr) - 1
    for i in range(len(arr)):
        value = sum(arr[i:])
        if value > 0 and matrix[i][check_idx] != '+':
            return False
        elif value < 0 and matrix[i][check_idx] != '-':
            return False
        elif value == 0 and matrix[i][check_idx] != '0':
            return False
    return True


def func(result):
    # 종료 조건 => 길이 N이면 종료
    if len(result) >= N:
        print(*result)
        exit()

    # 재귀 => idx 번째의 번호 정하기 | matrix[idx][idx]는 해당 숫자만 덧셈임
    idx = len(result)
    if matrix[idx][idx] == '+':
        seq_range = range(1, 11)
    elif matrix[idx][idx] == '-':
        seq_range = range(-10, 0)
    else:
        seq_range = range(0, 1)
    # seq_range 범위 값을 하나씩 넣어보기
    for num in seq_range:
        if check(result + [num]):
            func(result + [num])


# 문제의 matrix 그리기
N = int(input())
matrix = [[0] * N for _ in range(N)]
IN = list(input())
for i in range(N):
    for j in range(i, N):
        matrix[i][j] = IN.pop(0)
# 함수
func([])
