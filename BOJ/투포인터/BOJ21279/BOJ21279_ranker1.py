import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

N, C = map(int, input().split())
val_dict = {i: [] for i in range(100001)}

for _ in range(N):
    X, Y, V = map(int, input().split())
    val_dict[X].append((Y, V))

maxy = 100000
pick_list = [0] * 100001
value_list = [0] * 100001
cu_pick_cnt = 0
cu_val = 0
result = 0

for x in range(100001):
    for key in val_dict[x]:
        if key[0] <= maxy:
            cu_pick_cnt += 1
            cu_val += key[1]
            pick_list[key[0]] += 1
            value_list[key[0]] += key[1]

    while cu_pick_cnt > C:
        cu_pick_cnt -= pick_list[maxy]
        cu_val -= value_list[maxy]
        maxy -= 1
    result = max(result, cu_val)

print(result)
