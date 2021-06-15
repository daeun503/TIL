import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

def my_func(node):
    # 만약 tree[node] 값이 0이면 자식 노드를 합쳐줘야한다.
    if not tree[node]:
        # 오른쪽도 있으면 양쪽 합치고 없으면 왼쪽만
        if node*2+1 < N+1:
            tree[node] = my_func(node*2) + my_func(node*2+1)
        else:
            tree[node] = my_func(node*2)
    # if문 거쳤든 안거쳤든 이제 tree[node]에 값이 있으니 리턴
    return tree[node]


for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())

    # 트리 만들기. 인덱스:노드 번호, 벨류: 저장 값
    tree = [0] * (N+1)
    for _ in range(M):
        IN = list(map(int, input().split()))
        tree[IN[0]] = IN[1]

    my_func(1)
    print("#{} {}".format(tc, tree[L]))
