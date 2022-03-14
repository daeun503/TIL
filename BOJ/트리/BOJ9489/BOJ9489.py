import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


def func(k):
    # k의 부모 => 만약 부모가 없으면 루트 노드라서 k의 사촌 X
    k_parent = tree[k][0]
    if not k_parent:
        return 0
    # k의 형제
    k_sibling = tree[k_parent][1]
    # k의 부모의 부모 => 조상 => 만약 조상이 없으면 루트 노드라서 k의 사촌 X
    k_grandparent = tree[k_parent][0]
    if not k_grandparent:
        return 0
    # k의 조상의 자식 => k의 부모의 형제
    k_grandparent_child = tree[k_grandparent][1]
    # k의 부모의 형제의 자식 => k의 사촌
    k_grandparent_child_child = []
    for node in k_grandparent_child:
        k_grandparent_child_child.extend(tree[node][1])

    return len(k_grandparent_child_child) - len(k_sibling)


while 1:
    # 입력
    n, k = map(int, input().split())
    if n == 0:
        break
    IN = list(map(int, input().split()))

    # 트리 만들기 => 처음에 무조건 한 번은 if not is_child 에 들어가서 p = -1부터 시작
    current_parent, p = -1, -1
    tree = {IN[0]: [0, []]}
    for i in range(1, n):
        is_child = 0
        if IN[i] - IN[i-1] == 1:
            is_child = 1

        # 자식이 아니면 부모를 바꾼다
        if not is_child:
            p += 1
            current_parent = IN[p]
        tree[current_parent][1].append(IN[i])
        tree[IN[i]] = [current_parent, []]

    print(func(k))
