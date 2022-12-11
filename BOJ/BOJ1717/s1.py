import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


# 부모를 찾는 함수
# 부모로 자기 자신을 가리키면 자기를 리턴하고
# 부모로 다른 노드를 가리키면 그 노드를 찾아가서, 그 노드에서 부모를 다시 찾는다
def find(x):
    if p[x] == x:
        return x
    else:
        return find(p[x])


# 합집합
# y의 부모를 찾은 후, y 부모로 x 부모를 등록한다
def union(x, y):
    p[find(y)] = find(x)


n, m = map(int, input().split())
# 초기에 모든 노드는 부모로 자기 자신을 가리킨다
p = [i for i in range(n+1)]
for _ in range(m):
    flag, a, b = map(int, input().split())
    # 포함 되어있는지 확인
    if flag:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    # 합집합
    else:
        union(a, b)
