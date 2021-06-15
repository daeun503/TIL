"""
4. bfs - 1번 노드에서 가장 멀리 떨어진 노드 찾기 (dict)
거리에 대한 정보 담아 놓기
(필요하다면 기존에 작성한 내용을 복-붙 하셔도 됩니다!)
"""

def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = 0
    print("{}를 거리 표시".format(v))
    while queue:
        v = queue.pop(0)
        print("큐에서 {}를 꺼낸다. 현재 큐: {}".format(v, queue))
        for w in G.get(v, []):
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[v] + 1
                print("{}를 거리 표시".format(w))
    print("가장 멀리 떨어진 노드는 {} 입니다.".format(visited.index(max(visited))))

import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V,E = map(int, input().split())

# 간선 정보 초기화
IN = list(map(int, input().split()))

# Graph 초기화 (dict)
G = {}
for i in range(0, len(IN), 2):
    G[IN[i]] = G.get(IN[i], []) + [IN[i+1]]
print(G)

# 방문 표시 초기화
visited = [0] * (V+1)

# bfs 탐색 시작
bfs(1)
print("거리표시 {}".format(visited))