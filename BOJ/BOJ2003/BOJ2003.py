import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

N, M = map(int, input().split())
IN = list(map(int, input().split()))

DP = [0]*(N+1)
for i in range(1, len(IN)+1):
    DP[i] = DP[i-1] + IN[i-1]

i, j = 0, len(IN)
result = 0

# j 가 0이 될 때까지 반복
while j:
    if DP[j] - DP[i] == M:
        result += 1

    if i == j:
        j -= 1
        i = 0
    else:
        i += 1

print(result)