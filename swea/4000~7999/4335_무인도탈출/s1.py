import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 현재 k 번째 상자 쌓는 중. my_sum은 높이
def my_func(k, my_h, ca, cb):
    global result

    # 종료 조건
    if result < my_h:
        result = my_h

    # 가지치기
    if my_h + sum(check) <= result:
        return

    # 백트래킹
    for a, b, h, num in boxes:
        if check[num]:
            if (a <= ca and b <= cb):
                tmp = check[num]
                check[num] = 0
                my_func(k+1, my_h+h, a, b)
                check[num] = tmp
            elif (a <= cb and b <= ca):
                tmp = check[num]
                check[num] = 0
                my_func(k + 1, my_h + h, b, a)
                check[num] = tmp



for tc in range(1, int(input()) + 1):
    N = int(input())
    check = []
    boxes = []
    result = 0
    for _ in range(N):
        x, y, z = map(int, input().split())
        check.append(max(x, y, z))
        boxes.append((x, y, z, _))
        boxes.append((y, z, x, _))
        boxes.append((x, z, y, _))
    my_func(0, 0, 999999, 999999)
    print("#{} {}".format(tc, result))
    # print('#{} {}'.format(tc, result))

