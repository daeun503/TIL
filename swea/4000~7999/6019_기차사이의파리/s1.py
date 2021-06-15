import sys
sys.stdin = open("input.txt")

# D는 두 기차 전면부 사이의 거리, A는 기차 A의 속력, B는 기차 B의 속력, F는 파리의 속력
for tc in range(1, int(input())+1):
    D, A, B, F = map(int, input().split())
    # A, B가 충돌하기까지 몇 초 걸렸는지?
    time = D / (A+B)
    # 파리가 이동한 거리는 충돌하기까지의 시간 * 파리의 속도
    print("#{} {}".format(tc, time * F))