import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame
from collections import defaultdict

T = int(input())
n, A = int(input()), list(map(int, input().split()))
m, B = int(input()), list(map(int, input().split()))

# 배열 A의 0 ~ n 까지의 합
sum_A = [0] * (n+1)
sum_A[1] = A[0]
for i in range(2, n+1):
    sum_A[i] = sum_A[i-1] + A[i-1]

# 배열 A의 i ~ j 까지의 합
sub_sum_A = []
for i in range(1, n+1):
    for j in range(0, i):
        sub_sum_A.append(sum_A[i] - sum_A[j])

# 배열 B의 0 ~ m 까지의 합
sum_B = [0] * (m+1)
sum_B[1] = B[0]
for i in range(2, m+1):
    sum_B[i] = sum_B[i-1] + B[i-1]

# 배열 B의 i ~ j 까지의 합 => dict로 바로 접근
sub_sum_B = defaultdict(int)
for i in range(1, m+1):
    for j in range(0, i):
        sub_sum_B[sum_B[i] - sum_B[j]] += 1

# T - target 을 배열 B의 부분 합에서 찾으면 된다.
result = 0
for target in sub_sum_A:
    result += sub_sum_B[T - target]

print(result)
