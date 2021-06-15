import sys
sys.stdin = open("input.txt")

def in_order(node):
    if node <= V:
        in_order(node*2)
        print(tree[node], end='')
        in_order(node*2+1)

for tc in range(1, 11):
    V = int(input())
    tree = [0] * (V+1)

    for i in range(1, V + 1):
        IN = list(input().split())
        tree[int(IN[0])] = IN[1]

    print('#{}'.format(tc), end=' ')
    in_order(1)
    print()