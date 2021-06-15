import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    flag = 1
    for i in range(N):
        # M의 i번째 자리가 1이 아니면 flag = 0
        if not M & (1<<i):
            flag = 0
            break
    # flag가 아직 1이면 on, 0이면 off
    result = 'ON' if flag else 'OFF'
    print('#{} {}'.format(tc, result))