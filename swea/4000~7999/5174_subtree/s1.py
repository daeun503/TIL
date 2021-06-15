import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


def pre_order(n):
    global cnt
    if n:
        cnt += 1
        pre_order(tree[n][0])
        pre_order(tree[n][1])
    return cnt

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    IN = list(map(int, input().split()))
    tree = [ [0, 0, 0] for _ in range(E+2) ]
    for i in range(E):
        # 왼쪽 자식이 있으면 오른쪽에 추가 아니면 왼쪽
        if tree[IN[2*i]][0]:
            tree[IN[2*i]][1] = IN[2*i+1]
        else:
            tree[IN[2*i]][0] = IN[2*i+1]
        tree[IN[2*i+1]][2] = IN[2*i]
    cnt = 0
    print('#{} {}'.format(tc, pre_order(N)))
