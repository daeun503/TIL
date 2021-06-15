import sys
sys.stdin = open("input.txt")
from pandas import DataFrame




def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    p[find(a)] = find(b)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    cnt = 0
    for idx in range(len(p)):
        if idx == p[idx]:
            cnt += 1
    print("#{} {}".format(tc, cnt-1))