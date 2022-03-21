import sys
# input = sys.stdin.readline
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for _ in range(int(input())):
    t, k = map(int, input().split())
    # 노드 제거할 때 단말 노드일 때만 불가능. 나머지는 모두 가능
    if t == 1 and len(G[k]) == 1:
        print("no")
    else:
        print("yes")
