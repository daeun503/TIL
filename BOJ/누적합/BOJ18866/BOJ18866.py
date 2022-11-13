import sys
from pandas import DataFrame

sys.stdin = open("input.txt", "r")

N = int(input())
happy, tired = [], []
for _ in range(N):
    a, b = map(int, input().split())
    happy.append(a)
    tired.append(b)

if not sum(happy) and not sum(tired):
    print(N - 1)
    exit()

# 인덱스 k를 기준으로, 0~k까지는 행복도 h를 가지고 있어야하고
# 그 이후 k+1~는 행복도 h 미만을 가지고 있어야한다
# 정방향(->) 누적 happy_min는 idx의 최소 행복도 (젊은날의 최소)
# 역방향(<-) 누적 happy_max_reverse는 idx의 최대 행복도 (늙은날의 최대)
INF = float('inf')

happy_min, tired_max = [INF], [-INF]
for a, b in zip(happy, tired):
    if not a: a = INF
    if not b: b = -INF
    happy_min.append(min(happy_min[-1], a))
    tired_max.append(max(tired_max[-1], b))
happy_min.pop(0)
tired_max.pop(0)

happy_max_reverse, tired_min_reverse = [-INF], [INF]
for a, b in zip(happy[::-1], tired[::-1]):
    if not a: a = -INF
    if not b: b = INF
    happy_max_reverse.append(max(happy_max_reverse[-1], a))
    tired_min_reverse.append(min(tired_min_reverse[-1], b))
happy_max_reverse.pop(0); happy_max_reverse.reverse()
tired_min_reverse.pop(0); tired_min_reverse.reverse()

result = -2
for idx in range(N-1):
    check_happy = happy_min[idx] > happy_max_reverse[idx + 1]
    check_tired = tired_max[idx] < tired_min_reverse[idx + 1]
    if check_happy and check_tired:
        result = max(result, idx)
print(result + 1)
