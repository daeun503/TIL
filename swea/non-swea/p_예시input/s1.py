import sys
sys.stdin = open('input.txt')

# 1번 홀짝
N = int(input())
if N % 2:
    result = 1
else:
    result = 0
print(result)

# 2번 양수 합
N2 = map(int, input().split())
print(sum(N2))

# 3번 2행 2열 정수
N3 = int(input())
N3_list = []
for _ in range(N3):
    N3_list += [list(map(int, input().split()))]
print(N3_list[1][1])
