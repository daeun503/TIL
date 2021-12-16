import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


N, S = map(int, input().split())
IN = list(map(int, input().split()))

start, total, result = 0, 0, 100000

for end in range(len(IN)):
    total += IN[end]
    flag = 0
    while total >= S and start <= end:
        total -= IN[start]
        start += 1
        flag = 1
    if flag and result > end - (start-1):
        result = end - (start-1) + 1

if result == 100000:
    result = 0

print(result)
