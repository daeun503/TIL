import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 홀짝 구분해서 반으로 나누고, 길이 맞춰서 zip
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    IN = input().split()

    if N%2:      # 홀수일 때
        IN_A = IN[:len(IN) // 2 + 1]
        IN_B = IN[len(IN) // 2 + 1:] + ['']
    else:        # 짝수일 때
        IN_A = IN[:len(IN) // 2]
        IN_B = IN[len(IN) // 2:]

    result = []
    for a, b in zip(IN_A, IN_B):
        result += [a] + [b]

    print("#{}".format(tc), *result[:N] )