import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


# 더 작은 수를 부모로 만들기
# 사이클이 만들어졌으면 True 아니면 False
def union(x, y):
    p_x = find(x)
    p_y = find(y)
    if p_x == p_y:
        return True
    elif p_x < p_y:
        p[p_y] = p_x
    else:
        p[p_x] = p_y
    return False


n, m = map(int, input().split())
p = list(range(n))
for count in range(m):
    r, c = map(int, input().split())
    is_end = union(r, c)
    if is_end:
        print(count + 1)
        break
else:
    print(0)
