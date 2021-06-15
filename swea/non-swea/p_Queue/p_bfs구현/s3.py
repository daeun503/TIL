"""
3. bfs - 인접 딕셔너리 구현
(필요하다면 기존에 작성한 내용을 복-붙 하셔도 됩니다!)
"""

def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    print("{}를 방문 표시".format(v))
    while queue:
        v = queue.pop(0)
        print("큐에서 {}를 꺼낸다. 현재 큐: {}".format(v, queue))
        for w in G.get(v, []):
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1
                print("{}를 방문 표시".format(w))

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V,E = map(int, input().split())

# 간선 정보 초기화
IN = list(map(int, input().split()))

# Graph 초기화
G = {}
for i in range(0, len(IN), 2):
    G[IN[i]] = G.get(IN[i], []) + [IN[i+1]]
print(G)

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)
print(visited)