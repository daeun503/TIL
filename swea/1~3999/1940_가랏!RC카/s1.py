import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    vel = 0
    result = 0
    for i in range(N):
        IN = list(map(int, input().split()))

        if IN[0] == 0:        # 유지
            result += vel
        else:                 # 가속(1)/감속(2)
            if IN[0] == 1:    # 가속
                vel += IN[1]
            else:             # 감속
                vel -= IN[1]
                if vel <= 0:  # 속도가 0 이하이면 0으로
                    vel = 0
            result += vel

    print("#{} {}".format(tc, result))