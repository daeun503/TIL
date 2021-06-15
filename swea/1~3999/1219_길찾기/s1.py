import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 출발점은 0, 도착점은 99. DFS
for _ in range(1, 11):
    tc, N = map(int, input().split())
    L = [[] for _ in range(100)]
    IN = list(map(int, input().split()))

    # 연결 리스트
    for i in range(0, len(IN), 2):
        L[IN[i]].append(IN[i+1])

    # 시작노드와 방문 체크
    S = 0
    visited = [0] * 100
    visited[S] = 1

    # DFS. 스택 초기값
    stack = [S]
    while stack:
        v = stack.pop()
        # 인접 리스트에서 노드 하나씩 뽑으면서
        for w in L[v]:
            # 해당 노드에 아직 안갔으면 추가하고 방문 (마지막 노드로 v)
            if visited[w] == 0:
                visited[w] = 1
                stack.append(w)

    print("#{} {}".format(tc, visited[99]))