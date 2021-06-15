import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

# 컨테이너 수 N과 트럭 수 M
# 다음 줄에 N개의 화물이 무게wi
# 그 다음 줄에 M개 트럭의 적재용량 ti
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    w = sorted(list(map(int, input().split())))
    t = sorted(list(map(int, input().split())))

    result = 0
    while t and w:
        if t[-1] >= w[-1]:      # 트럭에 화물 운반 가능하면
            t.pop()             # 해당 트럭 없애고
            result += w.pop()   # result에 화물 더해주기
        else:                   # 운반 불가하면
            w.pop()             # 그냥 화물 버려주기

    print("#{} {}".format(tc, result))

