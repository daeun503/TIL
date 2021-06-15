import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = [0, 0, 0, 0, 0]

    # N이 1이 될 때까지 나누기. 한 회차에 여러번 나누도록 if문으로만
    while N != 1 :
        if N % 2 == 0:
            N = N // 2
            result[0] += 1
        if N % 3 == 0:
            N = N // 3
            result[1] += 1
        if N % 5 == 0:
            N = N // 5
            result[2] += 1
        if N % 7 == 0:
            N = N // 7
            result[3] += 1
        if N % 11 == 0:
            N = N // 11
            result[4] += 1

    # 언패킹 연산자 *
    print('#{}'.format(tc), *result)