import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    # 연결 리스트 만들기
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        G[i].append(j)
        G[j].append(i)

    # 시작과 끝 사이의 거리가 몇인지 판별, 안 연결이면 0
    S, E = map(int, input().split())

    visited = [-1] * (V+1)
    queue = [S]
    visited[S] = 0

    # 큐가 빌 때까지 반복
    while queue:
        v = queue.pop(0)
        for w in G[v]:
            # 방문 안했으면 큐에 넣어주고 방문하면서 거리는 이전 거리 + 1
            if visited[w] == -1:
                queue.append(w)
                visited[w] = visited[v] + 1

    print("#{} {}".format(tc, 0 if visited[E] == -1 else visited[E] ))