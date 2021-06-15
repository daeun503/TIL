import sys
sys.stdin = open("input.txt", "r")

T = int(input())
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 부분 집합 만들기
power_set = []
for i in range(1 << len(nums)):
    tmp = []
    for j in range(len(nums)):
        if i & (1 << j):
            tmp += [nums[j]]
    power_set.append(tmp)

# 부분집합의 길이가 N이고 합이 K이면 +1
for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0
    for i in power_set:
        if len(i) == N and sum(i) == K:
            result += 1

    print("#{} {}".format(tc, result))