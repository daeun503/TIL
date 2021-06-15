import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

def pre_order(node):
    global cnt
    if node:
        cnt += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])

for tc in range(1, int(input())+1):
    V, E, n1, n2 = map(int, input().split())
    IN = list(map(int, input().split()))
    ###################### 트리 만들기 ######################
    tree = [[0, 0, 0] for _ in range(V + 1)]
    for i in range(0, len(IN), 2):
        if tree[IN[i]][0]:  # 왼쪽 노드 차 있으면 오른쪽에 넣기
            tree[IN[i]][1] = IN[i+1]
        else:               # 왼쪽 노드 비어있으면 왼쪽에 넣기
            tree[IN[i]][0] = IN[i+1]
        tree[IN[i+1]][2] = IN[i] # 부모 체크
    #########################################################

    q1, q2 = tree[n1][2], tree[n2][2]      # q1, q2는 부모 노드
    qq1, qq2 = [q1], [q2]                  # qq1, qq2는 모든 부모 노드들
    while q1 or q2:                        # 루트 찍을 때까지 반복
        n1, n2 = q1, q2                    # 부모 노드를 현재 노드로 바꾸기
        q1, q2 = tree[n1][2], tree[n2][2]
        qq1.append(q1)                     # 부모(현재노드)의 부모를 qq1, qq2에 추가
        qq2.append(q2)                     # 이걸 반복

    # [-1]은 0이고(루트 노드의 부모) 그 전인 [-2]에 부모가 있는 쪽을 찾는다
    # 교집합을 통해 공통 부모가 몇 개 있는지 찾아서 뒤쪽부터 세면 됨
    if qq1[-2]:
        qqq_n = qq1[-len(set(qq1) & set(qq2))]
    else:
        qqq_n = qq2[-len(set(qq1) & set(qq2))]

    # 서브트리 순회하면서 노드 수 세기
    cnt = 0
    pre_order(qqq_n)
    print('#{} {} {}'.format(tc, qqq_n, cnt))








