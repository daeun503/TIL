import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

for _ in range(int(input())):

    N = int(input())
    IN = [list(map(int, input().split())) for _ in range(2)]

    if N == 1:
        print(max(IN[0][0], IN[1][0]))
        continue

    IN[0][1] += IN[1][0]
    IN[1][1] += IN[0][0]
    for i in range(2, N):
        IN[0][i] += max(IN[1][i - 1], IN[1][i - 2])
        IN[1][i] += max(IN[0][i - 1], IN[0][i - 2])
    print(max(IN[1][N - 1], IN[0][N - 1]))
