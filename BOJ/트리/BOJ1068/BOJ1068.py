import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


def count_leaf(node):
    childs = tree[node][1]
    result = 0
    # 노드에 자식이 없으면 리프노드
    if not childs:
        return 1
    # 있으면 재귀
    for child in childs:
        result += count_leaf(child)
    return result


N = int(input())
p = list(map(int, input().split()))
R = int(input())
root = 0

# [부모, 자식]
tree = [[-1, []] for _ in range(N)]
for node, p in enumerate(p):
    # node의 부모 체크
    tree[node][0] = p
    # 부모의 자식 리스트에 node 추가
    if p == -1:
        root = node
        continue
    tree[p][1].append(node)

# 제거할 노드의 부모
R_p = tree[R][0]
# 부모가 root면 답이 0
if R_p == -1:
    print(0)
    exit()
# 해당 부모와 제거할 노드의 연결을 제거
tree[R_p][1].remove(R)
print(count_leaf(root))
