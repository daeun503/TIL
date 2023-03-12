import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    X = find(x)
    Y = find(y)
    if X > Y:
        p[X] = Y
    elif X < Y:
        p[Y] = X

for tc in range(1, int(input()) + 1):
    n = int(input())
    k = int(input())
    p = list(range(n+1))
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)

    print(f"Scenario {tc}:")
    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        is_connect = find(u) == find(v)
        print(int(is_connect))
    print()
