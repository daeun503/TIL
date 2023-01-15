import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")


def find(a):
    if not p.get(a) or p.get(a) == a:
        return a
    return find(p[a])


def union(a, b):
    p_a, p_b = find(a), find(b)

    if p_a < p_b:
        p[p_b] = p_a
        count[p_a] = count.get(p_a, 1) + count.get(p_b, 1)
    elif p_a > p_b:
        p[p_a] = p_b
        count[p_b] = count.get(p_a, 1) + count.get(p_b, 1)


N = int(input())
p, count = dict(), dict()
for _ in range(N):
    IN = input().split()
    if IN[0] == "I":
        a, b = map(int, IN[1:])
        union(a, b)
    else:
        node = int(IN[1])
        value = count.get(find(node), 1)
        print(value)
