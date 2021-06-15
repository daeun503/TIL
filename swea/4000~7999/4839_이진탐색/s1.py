import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    # A count하기
    start = 1
    end = P
    A_cnt = 0
    while start <= end:
        middle = (start + end) // 2
        A_cnt += 1
        if A == middle: break
        elif A > middle: start = middle
        else: end = middle

    # B count하기
    start = 1
    end = P
    B_cnt = 0
    while start <= end:
        middle = (start + end) // 2
        B_cnt += 1
        if B == middle: break
        elif B > middle: start = middle
        else: end = middle

    if A_cnt > B_cnt:
        print('#{} B'.format(tc))
    elif A_cnt < B_cnt:
        print('#{} A'.format(tc))
    else:
        print('#{} 0'.format(tc))