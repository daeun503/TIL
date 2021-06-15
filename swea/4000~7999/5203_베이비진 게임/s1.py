import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


def my_func(who, num):
    global result
    who[num] += 1  # 숫자 카운트 올려주기

    # 트리플렛: 리스트 안에 3 있으면 끝
    if 3 in who:
        result = who[10]
        return

    # 런: 인덱스 0~9에 값이 있는게 3개 연속이면 끝 (3스택쌓기)
    stack = 0
    for j in range(10):
        stack = stack + 1 if who[j] else 0
        if stack == 3:
            result = who[10]
            return

for tc in range(1, int(input())+1):
    IN = list(map(int, input().split()))
    # A는 플레이어1, B는 플레이어 2. cnt 리스트 A, B
    A, B = [0]*10+[1], [0]*10+[2]
    result = 0
    for i in range(12):
        num = IN[i]
        # 홀수일때 플레이어2(B) 짝수일때 플레이어1(A)
        my_func(B, num) if i%2 else my_func(A, num)
        # for문 돌다가 result 값이 생기면 끝
        if result:
            break
    print("#{} {}".format(tc, result))
