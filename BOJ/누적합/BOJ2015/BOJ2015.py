import sys
sys.stdin = open('input.txt')
from collections import defaultdict

N, K = map(int, input().split())
IN = list(map(int, input().split()))

acc_dict = defaultdict(int)
acc_dict[0] = 1
acc, answer = 0, 0
for num in IN:
    acc += num
    answer += acc_dict[acc - K]
    acc_dict[acc] += 1

print(answer)
