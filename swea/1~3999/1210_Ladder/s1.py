import sys
sys.stdin = open('input.txt')
from pandas import DataFrame


# 상 좌 우
UP, L, R = (-1, 0), (0, -1), (0, 1)

def my_dir(r, c, dir):
    if dir == L and matrix[r + L[0]][c + L[1]] == 0: return UP
    if dir == R and matrix[r + R[0]][c + R[1]] == 0: return UP
    if dir == UP:
        if matrix[r + R[0]][c + R[1]]: return R
        elif matrix[r + L[0]][c + L[1]]: return L
    return dir

for _ in range(1, 11):
    tc = input()
    # 양 옆에 [0] 넣어줘서 my_dir에서 튀어나가는 거 막아주기
    matrix = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    # (99, 58(버퍼포함)) -> 한 칸 위 (98, 58(버퍼포함))부터 시작할 것 -> (0, c)가 목표
    finish_r = 99 - 1                    # 한칸 위 이동 - 1
    finish_c = matrix[99].index(2) + 0   # 한칸 위 이동 + 0
    rc_dir = UP

    # finish_r이 0이 되면 끝
    while finish_r:
        rc_dir = my_dir(finish_r, finish_c, rc_dir)
        finish_r += rc_dir[0]
        finish_c += rc_dir[1]

    # 맨 앞에 버퍼 추가했으니까 답은 column쪽에 -1 해주기
    print("#{} {}".format(tc, finish_c - 1))
