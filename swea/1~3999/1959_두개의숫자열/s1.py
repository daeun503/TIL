import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    # 더 짧은 쪽이 a, 더 긴 쪽이 b
    if a > b:
        a, b = b, a
        a_list, b_list = b_list, a_list

    # 마주보는 숫자 곱한 뒤 더하는 것 b-a+1 회 시행
    max_result = 0
    for i in range(b-a+1):
        # 한 회 시행했을 때의 결과 ouput
        output = 0
        for j in range(a):
            output += a_list[j] * b_list[i+j]
        # 한 회 시행했을 때마다 그 값이 max인지 확인
        if max_result < output:
            max_result = output

    print('#{} {}'.format(tc, max_result))