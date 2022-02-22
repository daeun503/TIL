import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

N = int(input())

DP = [[0]*10 for i in range(101)]
DP[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            DP[i][j] = DP[i-1][j+1]
        elif j == 9:
            DP[i][j] = DP[i-1][j-1]
        else:
            DP[i][j] = DP[i-1][j+1] + DP[i-1][j-1]

result = 0
for i in range(0, 10):
    result += DP[N][i]

print(result % 1000000000)
