import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")


def find(a):
    if p[a] == a:
        return a
    return find(p[a])


# 더 작은 값을 부모로 하기
def union(a, b):
    p_a, p_b = find(a), find(b)
    if p_a < p_b:
        p[p_b] = p_a
    else:
        p[p_a] = p_b


N = int(input())
p = list(range(N+1))
for _ in range(N-2):
    a, b = map(int, input().split())
    union(a, b)

# 부모가 다른 노드를 찾기
unlink_node = 0
for idx, value in enumerate(p):
    if not idx:
        continue
    # 부모가 1이 아니면 연결되지 않은 노드
    q_idx = find(idx)
    if q_idx != 1:
        unlink_node = idx
        break

print(1, unlink_node)
