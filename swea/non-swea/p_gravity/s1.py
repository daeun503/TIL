import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    box_list = list(map(int, input().split()))

    # 박스 수 만큼 떨어지는 거리 list 만들기
    fall_list = [0] * N

    for i in range(N):
        # 앞 박스가 뒷 박스보다 높으면 1만큼 떨어지는 것 반복
        for j in range(i+1, N):
            if box_list[i] > box_list[j]:
                fall_list[i] += 1

    print('#{} {}'.format(tc, max(fall_list)))