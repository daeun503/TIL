# import sys

# sys.stdin = open("input.txt", "r")


N, M = map(int, input().split())
sand = list(map(int, input().split())) + [0]
sand_delta = [0] * (N + 1)

for _ in range(M):
    start, end, delta = list(map(int, input().split()))
    sand_delta[start - 1] += delta
    sand_delta[end] -= delta

current = 0
for idx, delta in enumerate(sand_delta):
    current += delta
    sand[idx] += current

print(*sand[:-1])
