import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


def bfs(s):
    q = [s]
    # 방문했으면 0으로 바꾸기 (현재 1)
    visited = node_list[:]
    visited[s] = 0
    while q:
        v = q.pop(0)
        for w in tree[v][1]:
            if visited[w]:
                q.append(w)
                visited[w] = 0
    # 방문 안 한 곳이 남아있으면 값이 있음
    return sum(visited)


tc = 1
while 1:
    # input 받기
    IN = []
    node_zero_flag = 0
    while 1:
        IN.extend(map(int, input().split()))
        # input으로 마지막 0이 들어왔을 때
        if IN[-1] == 0:
            # 첫 번째도 0 이라서 0 0이 들어왔을 때 (노드가 0개)
            if IN[0] == 0:
                node_zero_flag = 1
            break
        # input으로 마지막 -1이 들어오면 완전히 종료
        elif IN[-1] == -1:
            exit()
    # 노드가 0개이면 트리인지 확인할 필요 X
    if node_zero_flag:
        print("Case {} is a tree.".format(tc))
        tmp = input()
        if tmp:
            break
        tc += 1
        continue

    # 트리인지 확인
    tree_flag = 1
    N, n = len(IN), max(IN)
    # 앞에는 부모, 뒤에 리스트는 자식
    tree = [[0, []] for _ in range(n+1)]
    # 노드 번호 체크
    node_list = [0] * (n+1)
    for i in range(0, N-2, 2):
        # u는 부모, v는 자식 (자식은 여러개 가능. 부모는 하나만)
        u, v = IN[i], IN[i+1]
        node_list[u] = node_list[v] = 1
        # 부모가 있는데 또 부모에 연결돼있으면 트리 X
        if tree[v][0]:
            tree_flag = 0
            break
        # 트리 맞으면 부모, 자식 연결
        tree[v][0] = u
        tree[u][1].append(v)

    # 루트 찾기
    root = 0
    for i in range(n+1):
        # 노드에 없는 번호면 패스
        if not node_list[i]:
            continue
        # 부모가 없는 노드면 루트인지 확인
        if not tree[i][0]:
            # 이미 루트로 지정한 노드가 있으면 두 개라서 트리X
            if root:
                tree_flag = 0
                break
            root = i

    # 루트가 아예 없으면 트리 X
    if not root:
        tree_flag = 0
    # 루트가 있으면 bfs 돌렸을 때 값 있으면 트리 X
    # bfs 탐색으로 모든 노드에 갈 수 있는지 확인
    elif bfs(root):
        tree_flag = 0

    # 출력 지정
    if tree_flag:
        print("Case {} is a tree.".format(tc))
    else:
        print("Case {} is not a tree.".format(tc))

    tmp = input()
    if tmp:
        break

    tc += 1
