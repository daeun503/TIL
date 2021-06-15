import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

for tc in range(1, int(input())+1):
    N = int(input())
    IN = [tuple(map(int, input().split())) for _ in range(N)]
    # 뒤로 갈수록 시작시각, 종료시각이 크니까 걸리는 시간 자체가 작음
    IN.sort()

    # 맨 뒤에서부터 센다. 맨 뒤에 있는 화물은 무조건 포함 가능(기준값)
    x, y = IN.pop()
    result = 1
    while IN:
        # 맨 뒤에 있는 화물의 종료시각(b)이 기준값의 시작 시간(x)보다 작아야한다
        a, b = IN[-1]
        if b > x:            # 크면은 그냥 버려주고
            IN.pop()
        else:                # 작으면 가능하니까 +1
            x, y = IN.pop()  # 새로운 기준으로 잡아준다
            result += 1
    print("#{} {}".format(tc, result))