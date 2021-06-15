"""
5. bfs - 재귀로 구현한 bfs
(필요하다면 기존에 작성한 내용을 복-붙 하셔도 됩니다!)
"""
queue = []
def bfs(v):
    visited[v] = 1
    print("{}를 방문 표시".format(v))
    for w in G[v]:
        if visited[w] == 0 and w not in queue:
            queue.append(w)
    # 큐가 빌 때까지 확인
    if queue:
        print("{}에서 맨 앞 요소를 꺼내서 재귀".format(queue))
        bfs(queue.pop(0))
    else:
        return

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V,E = map(int, input().split())

# 간선 정보 초기화
IN = list(map(int, input().split()))

# Graph 초기화
G = [[] for _ in range(V+1)]
for i in range(0, len(IN), 2):
    G[IN[i]].append(IN[i+1])
# print(G)

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)
print(visited)