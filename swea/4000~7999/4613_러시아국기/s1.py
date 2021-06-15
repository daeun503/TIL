import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

# 백트래킹 / 참고 4881 배열 최소합 => 4613 새로 칠해야 하는 칸의 개수의 최솟값
# my_sum이 최소여야한다. 그 중에서도 result가 최소일 때.
# (1), (2)를 안 썼더니 테케 실패.
def my_func(IN, pick, my_sum):
    global result
    r = len(pick)

    # 종료 조건
    # pick에 3종류가 아니면 버리고, my_sum이 result보다 작으면 새 값으로 갱신
    if r == len(IN):
        if len(set(pick)) != 3 : return  # (1)
        if result > my_sum: result = my_sum
        return

    # 유망성 검사
    # 지금 계산하고 있는 값(my_sum)이 기존 값(result) 보다 크면 버리기
    # pick에 3종류를 넣어야하는데 남은 자리에 3종류 못 넣을거같으면 버리기
    if my_sum >= result: return
    if 3 - len(set(pick)) > len(IN) - len(pick): return  # (2)

    # 재귀
    # pick가 비어있으면 0 부터 넣고, 차 있으면 [-1] 값이랑 넣으려는 값 차이가 1이하여야 함
    for c in range(3):
        if pick:
            if 0 <= c - pick[-1] <= 1:
                my_func(IN, pick + [c], my_sum + IN[r][c])
        else:
            if c == 0 :
                my_func(IN, pick + [c], my_sum + IN[r][c])

    # 결과 리턴
    return result


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    IN = []
    # IN = [W줄로 만들기 위해 칠해야하는 개수, B줄로 ~ , R줄로 ~ ]
    # => IN값들의 합이 최소여야한다.
    for _ in range(N):
        i = list(input())
        IN += [[M - i.count('W'), M - i.count('B'), M - i.count('R')]]
    result = 99999999
    print("#{} {}".format(tc, my_func(IN, [], 0)))