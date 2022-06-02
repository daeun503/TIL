# import sys
# sys.stdin = open("input.txt", "end")
from collections import deque


def topology_sort():
    result = []
    q = deque()
    
    # 시작 전에 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복 
    while q:
        now = q.popleft()
        result.append(now)
        # 연결된 노드들의 진입 차수에서 1 빼고, 0이 되면 큐에 넣기
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)    

    return result


N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
# 정점a에서 b로 이동 가능 & 진입 차수 증가
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

print(*topology_sort())