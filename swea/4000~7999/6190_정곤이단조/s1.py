import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


def my_func(IN):
    result = -1
    for i in range(len(IN)):
        for j in range(i + 1, len(IN)):

            # num이 단조 증가인지 감소인지 판단
            num = str(IN[i] * IN[j])
            for k in range(len(num) - 1):
                if int(num[k]) > int(num[k + 1]):
                    break
            # 단조 증가하면
            else:
                if result < int(num):
                    result = int(num)
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    IN = list(map(int, input().split()))

    print("#{} {}".format(tc, my_func(IN)))