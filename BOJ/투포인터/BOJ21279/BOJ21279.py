import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

# 이 코드는 잘못된 코드 => 다시 풀기
N, C = map(int, input().split())
result = 0
MAX_X = 0

pos = {}
y_list, x_list = [], []
for _ in range(N):
    x, y, v = map(int, input().split())
    pos[(y, x)] = v
    x_list.append(x)
    y_list.append(y)
    MAX_X = max(MAX_X, y)

MAX_X += 1
top = [[0, 0] for _ in range(MAX_X)]
bottom = [[0, 0] for _ in range(MAX_X)]

for y in y_list:
    for x in x_list:
        value = bottom[x][1] + pos.get((y, x), 0) + (top[x-1][1] - bottom[x-1][1])
        cost = bottom[x][0] + bool(pos.get((y, x), 0)) + (top[x-1][0] - bottom[x-1][0])
        top[x] = [cost, value]
        if cost <= C:
            result = max(result, value)
        else:
            break
    bottom = top
    top = [[0, 0] for _ in range(MAX_X)]

print(result)
