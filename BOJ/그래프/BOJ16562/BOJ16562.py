# import sys
# sys.stdin = open("input.txt", "r")


def find(child):
    if parents[child] == child:
        return child
    else:
        return find(parents[child])


def union(v, w):
    v_parent = find(parents[v])
    w_parent = find(parents[w])
    v_parent_fee = fees[v_parent]
    w_parent_fee = fees[w_parent]
    # v의 친구 비용이 w친구 비용보다 크면, w와 친구가 이득 (=v의 부모를 w로) + v 비용 신경 X
    if v_parent_fee > w_parent_fee:
        fees[v_parent] = 0
        parents[v_parent] = w_parent
    # 반대면 v와 친구하는 것이 이득 (=w의 부모를 v로) + w 비용 신경X
    else:
        fees[w_parent] = 0
        parents[w_parent] = v_parent


N, M, k = map(int, input().split())
fees = list(map(int, input().split()))

# v, w를 묶는다
parents = list(range(N))
for _ in range(M):
    v, w = map(int, input().split())
    union(v-1, w-1)

# 친구할 수 있으면 비용, 없으면 Oh no
total_fee = sum(fees)
if k >= total_fee:
    print(total_fee)
else:
    print("Oh no")
