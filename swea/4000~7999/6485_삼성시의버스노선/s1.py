import sys
sys.stdin = open('input.txt')

# N: 버스노선 | i번째 버스 노선(bus_line): 번호 Ai이상 Bi이하인 정류장만 다니는 노선
# P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 ?

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus_line = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    c_line = [int(input()) for _ in range(P)]

    # c번 버스가 다니는 노선 모두 구해주기
    result = [0] * 5002
    for th_bus in bus_line:
        for c in range(th_bus[0], th_bus[1] + 1):
            result[c] += 1

    # 문제에서 물어보는 c번 버스 정류장 지나는 노선 개수만 구해주기
    a = [result[c] for c in c_line]
    print('#{}'.format(tc), *a)

    # 언패킹 안 쓸거면 이거
    # print('#{}'.format(tc), end=' ')
    # for c in c_line:
    #     print(result[c], end=' ')
    # print(' ')

