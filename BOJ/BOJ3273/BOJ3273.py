import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame
from copy import deepcopy

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
result = 0

# start, end 포인터
s, e = 0, n-1
arr.sort()

while s < e:

    # start + end 의 합 pair_sum
    pair_sum = arr[s] + arr[e]

    # 합이 x 이면 +1 // start, end 이동
    if pair_sum == x:
        result += 1
        s += 1
        e -= 1

    # 합이 x 보다 작으면 start를 오른쪽으로
    elif pair_sum < x:
        s += 1

    # 합이 x 보다 크면 end를 왼쪽으로
    else:
        e -= 1

print(result)
