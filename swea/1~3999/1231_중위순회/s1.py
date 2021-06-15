import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

def in_order(node):
    if node:
        in_order(tree[node][0])
        print(tree[node][3], end='')
        in_order(tree[node][1])

for tc in range(1, 11):
    V = int(input())
    tree = [[0, 0, 0, 0] for _ in range(V + 1)]    # [왼쪽, 오른쪽, 부모, 나]

    for i in range(1, V+1):
        IN = list(input().split())
        if len(IN) == 4:
            n, w, s1, s2 = int(IN[0]), IN[1], int(IN[2]), int(IN[3])
            # tree[n] = [s1, s2, 0, w] 로 안 쓴건 [2]가 덮어쓰여질 수 있어서
            tree[n][0] = s1    # 왼쪽 자식 노드
            tree[n][1] = s2    # 오른쪽 자식 노드
            tree[n][3] = w     # 내 알파벳
            tree[s1][2] = n    # V=s1의 부모노드 n
            tree[s2][2] = n    # V=s2의 부모노드 n
        elif len(IN) == 3:
            n, w, s1 = int(IN[0]), IN[1], int(IN[2])
            tree[n][0] = s1    # 왼쪽 자식 노드
            tree[n][3] = w     # 내 알파벳
            tree[s1][2] = n    # V=s1의 부모노드 n
        else:
            n, w = int(IN[0]), IN[1]
            tree[n][3] = w     # 내 알파벳

    print('#{}'.format(tc), end=' ')
    in_order(1)
    print()





