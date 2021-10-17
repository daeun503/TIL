import sys
sys.stdin = open('input.txt')


# 에라토스테네스 체 리스트 버전
prime = [1] * 1000001
prime[0] = 0
prime[1] = 0
for i in range(2, 500001):
    if prime[i]:
        for j in range(2*i, 1000001, i):
            prime[j] = 0

for tc in range(int(input())):
    N = int(input())
    result = 0
    for i in range(2, N//2+1):       # 절반까지 확인
        if prime[i] and prime[N-i]:  # i가 소수, N-i가 소수면
            result += 1              # 답 += 1
    print(result)


# set 버전 ////////// 이게 더 오래걸림
n = 1000000
# prime = set(range(2, n+1))
# for i in range(2, n//2+1):
#     if i in prime:
#         prime -= set(range(2*i, n+1, i))
#
# for tc in range(int(input())):
#     N = int(input())
#     result = 0
#     for i in range(2, N//2+1):
#         if i in prime and N-i in prime:
#             result += 1
#     print(result)
