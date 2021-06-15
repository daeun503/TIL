"""
연습 문제2. dfs 구현
 - dfs 방식으로 그래프를 탐색하시오.
 - 알고리즘 구현은 반복과 재귀를 사용하시오.
"""

#1. 반복문
def dfs_iteration(s):
    stack = [s]
    visited[s] = 1
    while stack:
        v = stack.pop()
        print(v, '방문')
        for w in range(V+1):
            if G[v][w] and not visited[w]:
                visited[w] = 1
                stack.append(w)

#2. 재귀 함수
def dfs_recursion(v):
    visited[v] = 1
    print(v, '방문')
    for w in range(V+1):
        if G[v][w] and not visited[w]:
            dfs_recursion(w)


import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

# 정점, 간선 정보 초기화
V, E = map(int, input().split())

# 그래프, 방문 정보 초기화
IN = list(map(int, input().split()))
visited = [0] * (V+1)

# 그래프 그리기
G = [[0]*(V+1) for _ in range(V+1)]
for i in range(0, len(IN), 2):
    G[IN[i]][IN[i+1]] = 1
    G[IN[i+1]][IN[i]] = 1

# 탐색 시작
dfs_iteration(1)
print('----------------')
visited = [0] * (V+1)
dfs_recursion(1)