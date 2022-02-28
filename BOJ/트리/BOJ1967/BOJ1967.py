import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
# 노드가 n <= 10000개라서 10000번 재귀 가능
sys.setrecursionlimit(10000)

def max_sub_tree(node):
    length_list = [0, 0]

    # 내 자식들
    for child, weight in G[node][1]:
        # 내 자식이 리프노드면
        if not G[child][1]:
            length_list.append(weight)
            continue
        # 내 자식이 리프노드가 아니면
        length_list.append(max_sub_tree(child) + weight)

    # DP = 해당 노드를 root로 해서 최대 지름
    length_list.sort()
    DP[node] = length_list[-1] + length_list[-2]
    # 리턴할 때는 최대값을 리턴
    return length_list[-1]


n = int(input())
DP = [0] * (n+1)

G = [[0, []] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    G[c][0] = p
    G[p][1].append((c, w))

max_sub_tree(1)

print(max(DP))
