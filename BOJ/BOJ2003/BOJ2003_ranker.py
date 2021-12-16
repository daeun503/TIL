import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
IN = list(map(int, input().split()))
k, total, result = 0, 0, 0

for i in IN:
    total += i
    while total > M:
        total -= IN[k]
        k += 1
    result += (total == M)

print(result)
