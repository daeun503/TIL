import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

N = int(input())

# 1. 입력받기

# 1-1 첫번째 방법
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
print(matrix)

# 1-2 두번째 방법
matrix = [0] * N
for i in range(N):
    matrix[i] = list(map(int, input().split()))
print(matrix)

# 1-3 세번째 방법
matrix = [list(map(int, input().split())) for _ in range(N)]
print(matrix)


# 2. 행 우선
for i in range(N):
    for j in range(N):
        print(matrix[i][j])
# 3. 열 우선
for i in range(N):
    for j in range(N):
        print(matrix[j][i])
# 4. 지그재그
for i in range(N):
    for j in range(N):
        print(matrix[i][j + (N-1-2*j) * (i%2)])
# 5. 전치행렬
for i in range(N):
    for j in range(N):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]