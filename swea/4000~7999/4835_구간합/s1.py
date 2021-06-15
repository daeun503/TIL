import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# N: 정수가 들어있는 배열의 길이 M: 구간합 몇 개 할 것 인지
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    # 0부터 N-M까지 i 순회하면서 i~i+M-1까지 합 구한 뒤 리스트로 만들기
    hap_list = [sum(num_list[i:i+M]) for i in range(N-M+1)]

    print('#{} {}'.format(tc, max(hap_list) - min(hap_list)))