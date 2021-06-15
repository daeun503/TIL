import sys
sys.stdin = open('input.txt')
from pandas import DataFrame



# 모든 정점에서 bfs 한 후 최대값을 반환하면 되지 않을까? 했는데
# 1갈래 -> 2갈래 -> 1갈래 라고 하면 1갈래로 다시 통합될 때 방문 처리돼서 깊게 못갈 수 있다

def dfs(v, dist):
    global dist_max

    if dist > dist_max:
        dist_max = dist

    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            dfs(w, dist+1)
    visited[v] = 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]

    result = 0
    for _ in range(M):
        x, y = map(int, input().split())
        G[x].append(y)
        G[y].append(x)

    dist_max = 0
    # for문의 dfs한 번 끝날 때 visited 0으로 돌아와서
    # 매번 새로 써줄 필요 X 한번만 써줘도 됨
    visited = [0] * (N + 1)
    for s in range(1, N+1):
        dfs(s, 1)

    print("#{} {}".format(tc, dist_max))


'''


import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

def dfs(v, dist):
    global dist_max

    # 만약에 현재 dist가 dist_max보다 크면 갱신
    ???

    # v를 방문 표시
    ???
    # v에 연결된 w에 갈 수 있고, 아직 방문하지 않았으면
    # 해당 w를 시작 정점으로 다시 dfs 탐색
    ???
    # v를 방문 표시 해제
    ???


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    ########## 인접 행렬 만들기 ##########
    # G 초기화
    G = ???
    # x, y를 input에서 받아서 인접행렬 G에 표시해주기
    for _ in range(M):
        x, y = map(int, input().split())
        ???
    # 인접행렬 G 출력
    print(DataFrame(G))


    ###### 모든 노드에 대해서 dfs 탐색 ######
    # 최장 거리 변수
    dist_max = 0
    # 방문 표시
    visited = [0] * (N + 1)
    # 모든 노드 (1~N)에 대해서 dfs 탐색
    for s in range(1, N+1):
        dfs(s, 1)

    print("#{} {}".format(tc, dist_max))
        
        '''