import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    L = [[] for _ in range(V+1)]

    # 인접 리스트 생성
    for _ in range(E):
        v, w = map(int, input().split())
        L[v].append(w)

    # 경로의 존재를 확인할 출발 노드 S와 도착노드 G
    S, G = map(int, input().split())

    # 방문 체크
    visited = [0] * (V+1)

    # 시작 노드와 방문 체크
    stack = [S]
    visited[S] = 1

    while stack:
        v = stack.pop()
        # 인접 리스트에서 노드 하나씩 뽑으면서
        for w in L[v]:
            # 해당 노드에 아직 안갔으면 추가하고 방문 (마지막 노드로 v)
            if visited[w] == 0:
                stack.append(w)
                visited[w] = 1

    print("#{} {}".format(tc, visited[G]))