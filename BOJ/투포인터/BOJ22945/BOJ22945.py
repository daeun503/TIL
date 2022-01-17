import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

N = int(input())
IN = list(map(int, input().split()))

p1, p2 = 0, N-1
result = 0

while p1 < p2:
    # 최대값 갱신
    dist = p2 - p1 - 1
    result = max(result, dist * min(IN[p1], IN[p2]))

    # p2가 더 크면 p1을 바꿔야하니까 p1 +1
    if IN[p1] <= IN[p2]:
        p1 += 1
    # p1이 더 크면 p2를 바꿔야하니까 p2 -1
    else:
        p2 -= 1

print(result)
