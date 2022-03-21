import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from pandas import DataFrame


def bfs(n):
    visited = [0] * (V+1)
    q = [n]
    visited[n] = 1
    while q:
        v = q.pop(0)
        for w, dist in tree[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + dist

    # 출력할 때 dist 시작 값이 1이라 dist 값은 1 빼줘야 함
    max_dist = max(visited)
    max_node = visited.index(max_dist)

    return max_node, max_dist


V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V):
    IN = list(map(int, input().split()))
    n1 = IN[0]
    i = 1
    while IN[i] != -1:
        n2, dist = IN[i], IN[i+1]
        tree[n1].append((n2, dist))
        i += 2

check = [0] * (V+1)
result = 0
# 임의의 노드에서 가장 먼 노드를 구한다
# 가장 먼 노드에서 가장 먼 노드를 구하면 트리의 지름
max_node, max_dist = bfs(1)
max_node, max_dist = bfs(max_node)
print(max_dist - 1)
