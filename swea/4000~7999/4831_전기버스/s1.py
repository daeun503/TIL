import sys
sys.stdin = open("input.txt", "r")


# K: 최대 이동 정류장 수, N: 종점 정류장, M: 충전기 정류장 수 charge: 충전기 정류장
def func(K, N, M, charge):
    energy = K
    result = 0
    charge_idx = -1

    # 위치 이동할 때마다 에너지 1씩 감소
    for posit in range(1, N + 1):
        energy -= 1

        # 만약 충전소에 도착하면 충전소 인덱스 증가시켜주기
        if posit in charge:
            charge_idx += 1

            # 마지막 충전소일 때 (아래와 한번에 묶으면 charge_idx+1 에서 인덱스에러)
            if charge[charge_idx] == charge[-1]:
                # 마지막 충전소인데 종점까지 거리가 에너지보다 많이 남았으면 충전
                if N - charge[-1] > energy:
                    energy = K
                    result += 1

            # 마지막 충전소가 아닌데, 다음 충전소까지의 거리가 에너지보다 많이 남았으면 충전
            elif charge[charge_idx + 1] - charge[charge_idx] > energy:
                energy = K
                result += 1

        # 종점 도착하면 충전 횟수 리턴, 종점 도착 안했는데 에너지 떨어졌으면 0 리턴
        if posit == N:
            return result
        elif energy <= 0:
            return 0


T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    print('#{} {}'.format(tc, func(K, N, M, charge)))