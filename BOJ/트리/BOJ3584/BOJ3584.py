import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


# 자신부터 부모로 거슬러 올라가면서 parents 에 넣는다
def search_parents(node):
    parents = []
    while node:
        parents.append(node)
        node = tree[node][0]
    return parents


T = int(input())
for _ in range(T):
    N = int(input())
    tree = [[0, []] for _ in range(N+1)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        tree[B][0] = A
        tree[A][1].append(B)
    n1, n2 = map(int, input().split())

    # 노드 n1, n2의 부모 리스트를 생성
    n1_parents = search_parents(n1)
    n2_parents = search_parents(n2)

    # 노드 n1의 부모 리스트를 앞에서부터 확인하면서
    # 공통 조상이 있으면 break
    for num in n1_parents:
        if num in n2_parents:
            print(num)
            break

