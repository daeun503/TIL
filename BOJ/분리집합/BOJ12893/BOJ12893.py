import sys

input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def union(A, B):
    A = find(A)
    B = find(B)
    if A != B:
        p[B] = A


N, M = map(int, input().split())
p = list(range(N+1))
enemy = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())  # 서로 적
    A, B = find(A), find(B)

    # 적끼리 같은 그룹이면 이론 성립 X
    if A == B:
        print(0)
        break

    # a의 적과 b를 동지로 설정
    if a_enemy := enemy[A]:
        union(a_enemy, B)
    else:
        enemy[A] = B

    # b의 적과 a를 동지로 설정
    if b_enemy := enemy[B]:
        union(b_enemy, A)
    else:
        enemy[B] = A
else:
    print(1)
