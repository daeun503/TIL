import sys
from collections import defaultdict
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    X = find(x)
    Y = find(y)
    if X > Y:
        p[X] = Y
    elif X < Y:
        p[Y] = X


# 모든 지점을 지나면서 모든 연결 구간들을 지나고 싶어한다.
V, E = map(int, input().split())
p = list(range(V + 1))
count = defaultdict(int)
route = defaultdict(int)
for _ in range(E):
    Va, Vb = map(int, input().split())
    if Va > Vb:
        Va, Vb = Vb, Va
    # 꼭지점의 차수를 세준다
    count[Va] += 1
    count[Vb] += 1
    # 이들을 연결해준다
    union(Va, Vb)
    # route에 중복 체크 ex. (1, 2) 나오면 (2, 1)은 안됨
    # 근데 이거 없어도 통과함
    route[f"{Va}to{Vb}"] += 1
    if route[f"{Va}to{Vb}"] == 2:
        print("NO")
        exit()

# 모든 노드의 부모가 1인지 체크
check = all(find(v) == 1 for v in range(1, V + 1))
# check = all(value == 1 for value in p[1:]) 이렇게 하니까 틀림
# 홀수 차수의 개수를 카운트
odd_count = 0
for key, value in count.items():
    if value % 2:
        odd_count += 1

# 모든 노드를 통과하지 않으면 NO
if not check:
    print("NO")
# 홀수 차수가 1이거나, 3이상이면 NO (0이나 2만 Ok)
elif odd_count == 1 or odd_count > 2:
    print("NO")
else:
    print("YES")
