import sys
sys.stdin = open("input.txt")


def in_order(node):
    # [1]이 0이면 피연산자([숫자, 0, 0]) 이므로 바로 리턴
    if tree[node][1] == 0:
        return tree[node][0]
    # [1]이 0이 아니면 연산 노드
    if node:
        a = in_order(tree[node][1])
        v = tree[node][0]
        b = in_order(tree[node][2])
    # 연산자 맞춰서 연산 리턴
    if v == '+': return a+b
    elif v == '-': return a-b
    elif v == '*': return a*b
    elif v == '/': return a/b

for tc in range(1, 11):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N+1)]
    # 트리 만들기: 연산노드는 [연산자, 자식1, 자식2] 피연산자는 [숫자, 0, 0]
    for _ in range(N):
        IN = input().split()
        # IN[1]이 숫자면 [0]에 숫자 넣고, 아니면 str형태로 넣기
        tree[int(IN[0])][0] = int(IN[1]) if IN[1].isdigit() else IN[1]
        # input에 2, 3인덱스 있으면(연산노드의 자식) 트리에 추가해주기
        for i in range(2, len(IN)):
            tree[int(IN[0])][i-1] = int(IN[i])

    result = int(in_order(1))
    print("#{} {}".format(tc, result))