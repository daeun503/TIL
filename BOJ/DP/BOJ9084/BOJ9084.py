import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    DP = [0] * (M+1)
    DP[0] = 1

    # DP[x] = DP[x - coin1] + DP[x - coin ] ... + DP[x - coin...]
    # x - coin 으로 하니까 음수가 돼서, i + coin 으로 치환
    for coin in coins:
        for i in range(M - coin + 1):
            DP[i + coin] += DP[i]

    print(DP[M])
