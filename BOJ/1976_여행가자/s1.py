import sys
sys.stdin = open('input.txt')



def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(a, b):
    p[find(b)] = find(a)


N = int(input())
M = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
plans = list(map(int, input().split()))

p = [i for i in range(N)]
for r in range(N):
    for c in range(N):
        if matrix[r][c]:
            union(r, c)


# 아 ! 이거 대표노드 왜 안되는가 했는데
# plan에 없는 노드가 대표노드일 수 있겠구나..
# root_cnt = 0
# for plan in plans:
#     if p[plan-1] == plan-1:
#         root_cnt += 1
# print("YES") if root_cnt == 1 else print('NO')

# plan중 하나의 루트를 찾고 plan들의 루트가 같으면 YES
root = find(plans[0]-1)
for plan in plans:
    if find(plan-1) != root:
        print("NO")
        break
else:
    print("YES")

# 아니면 이것도 가능
# root = set()
# for plan in plans:
#     root.add(find(plan-1))
# print("YES") if len(root) == 1 else print('NO')
