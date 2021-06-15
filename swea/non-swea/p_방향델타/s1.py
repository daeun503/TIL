import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
print(DataFrame(matrix))

# 현재 위치 -> (1, 1)
x = 1
y = 1

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(4):
    # x: 기존의 위치 / dx: x의 변화
    # 결국 nx는 기존위치 x에서 dx[i]만큼 이동한 것
    nx = x + dx[i]
    # y: 기존의 위치 / dy: y의 변화
    # 결국 ny는 기존위치 y에서 dy[i]만큼 이동한 것
    ny = y + dy[i]

    # 백. 만약 새로운 x의 위치가 0보다 작거나 N보다 크거나 같거나
    if nx < 0 or nx >= N or ny < 0 or ny >= N: continue

    print(matrix[nx][ny])