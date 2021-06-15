import sys
sys.stdin = open("input.txt")

T = int(input())

# N: 오는 사람 수, M초의 시간을 들여 K개의 붕어빵을 만든다.
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    IN = list(map(int, input().split()))
    IN.sort()
    result = 'Possible'

    # 시간, 빵, 몇 번째 사람인지, flag변수 (이중 while문 종료)
    time, bread, people, flag = 0, 0, 0, 0

    while people != N:
        # 한 타임 시간이 지났다고 치자
        time += M
        # 한 타임 빵 만들기 전에 사람이 오면
        while people < len(IN) and time > IN[people]:
            # 빵이 있으면 빵 하나 주고, 다음 사람
            if bread:
                bread -= 1
                people += 1
            # 빵이 없으면 불가능, flag 1로 이중 while문 종료
            else:
                result = 'Impossible'
                flag = 1
                break
        # 한 타임 시간 지났을 때 만든 빵 더해주기
        bread += K
        # flag 변수: 이중 while문 종료
        if flag: break

    print("#{} {}".format(tc, result))