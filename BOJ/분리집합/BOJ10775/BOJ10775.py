import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")


def docking(node: int) -> bool:
    # node가 "비어있는 노드"라고 가리키고 있는 것
    empty_node = p[node]
    # 근데 그 비어있는 노드가 0 이거나, 실은 안 비어있을 수 있음
    # 그럼 -1 해서 이전 노드를 확인 (이전 노드가 가리키는 비어있는 노드)
    while empty_node and dock[empty_node]:
        empty_node -= 1
        empty_node: int = p[empty_node]

    # 비어있는 노드가 있으면 방문 체크해주고
    # 처음 입력받은 노드와 비어있는 노드가 가리키는 곳은 -1로 해줌
    if empty_node:
        dock[empty_node] = 1
        p[node] = p[empty_node] = empty_node - 1
        return True
    else:
        return False


G = int(input())
P = int(input())
dock = [0] * (G+1)
p = list(range(G+1))

count = 0
for _ in range(P):
    g = int(input())
    success = docking(g)
    if success:
        count += 1
    else:
        print(count)
        exit()
print(count)
