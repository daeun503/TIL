import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

def calc(cur_n, i):
    if i == 0:
        return cur_n + 1
    elif i == 1:
        return cur_n - 1
    elif i == 2:
        return cur_n * 2
    else:
        return cur_n - 10


for tc in range(1, int(input())+1):
    # N을 M으로 만들기 위해 몇 번의 연산?
    N, M = map(int, input().split())
    Q = [0] * 1000000
    memo = [-1] * 1000001

    rear, front = 0, 0
    cur_n, cur_cnt = N, 0
    memo[cur_n] = 0

    while memo[M] == -1 :
        for i in range(4):
            next_n = calc(cur_n, i)
            # 범위 안에 들어오는 연산이고(중간 연산 결과도 100만 이하) 아직 계산이 안되어 있다면(=> memo[next_n] == -1)
            if 0 < next_n <= 1000000 and memo[next_n] == -1:
                memo[next_n] = memo[cur_n] + 1   # 값 계산하고
                rear += 1                        # 다음 값을 받기 위해 증가 시키고
                Q[rear] = (next_n, cur_cnt + 1)  # 연산 횟수 누적 시키기(cur_cnt + 1)

        front += 1
        cur_n, cur_cnt = Q[front]

    print("#{} {}".format(tc, memo[M]))