import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    p[find(y)] = find(x)


n, m = map(int, input().split())
p = [i for i in range(n+1)]
for _ in range(m):
    flag, a, b = map(int, input().split())
    # 포함 되어있는지 확인
    if flag:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    # 합집합
    else:
        union(a, b)
