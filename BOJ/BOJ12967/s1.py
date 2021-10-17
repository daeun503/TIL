import math
import sys

sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
A = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

result = 0
for i in range(N-2):
    target_i = K // math.gcd(A[i], K)
    if target_i == 1:
        result += (N-(i+1)-1)*(N-(i+1))//2
    elif A[i+1]*A[i+2] >= target_i:
        for j in range(i+1, N-1):
            target_j = target_i // math.gcd(A[j], target_i)
            if target_j == 1:
                result += N-(j+1)
            elif A[j+1] >= target_j:
                result += A[j+1:].count(target_j)
print(result)





'''
N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
result = 0
pick = [0, 0, 0] # pqr리스트
print(result)



def my_func(idx):
    global result

    # 종료 조건
    if idx == 3:
        if A[pick[0]]*A[pick[1]]*A[pick[2]] % K == 0:
            result += 1
        return

    # 유망성 검사
    if A[pick[0]] % K == 0:
        result += (N-pick[0]-1)*(N-pick[0]) // 2
        return
    elif A[pick[0]]*A[pick[1]] % K == 0:
        result += N - pick[1]
        return




    # 재귀
'''
