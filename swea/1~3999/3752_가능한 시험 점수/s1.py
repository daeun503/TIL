import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


# 동윤님 코드 보고 공부!
for tc in range(1, int(input())+1):
    N = int(input())
    IN = list(map(int, input().split()))
    result = [1] + [0]*sum(IN)
    result[0] = 1
    cases = [0]

    for i in range(N):
        for j in range(len(cases)):
            new = IN[i] + cases[j]
            if result[new] == 0:
                result[new] = 1
                cases.append(new)

    print("#{} {}".format(tc, sum(result)))


# swea에서 찾은 거
for tc in range(1, int(input())+1):
    N = int(input())
    IN = list(map(int, input().split()))
    a = 1
    for i in IN:
        a |= a << i
    print("#{} {}".format(tc, bin(a).count('1')))