import sys
sys.stdin = open('input.txt')



A = [0] * 5001
A[0] = 1
A[2] = 1
A[4] = 2

def my_func(L):
    global A

    if not A[L-2]:
        A[L-2] = my_func(L-2)

    if A[L] == 0:
        A[L] += A[L-2]                 # (S)의 갯수 = A[L-2]
        for s in range(2, L, 2):       # ST 의 갯수=()ST / ST() 기타 등등 중복
            A[L] += A[s] * A[L-2 - s]  # L=8: ST=6: (S,T)=(2,4),(4,2)

    # 정석: 카탈랑 수/ 이쪽이 더 빠름
    # if A[L] == 0:
    #     for s in range(0, L, 2):
    #         A[L] += A[s] * A[L-s-2]

    return A[L] % 1000000007


for tc in range(int(input())):
    L = int(input())
    print(0) if L%2 else print(my_func(L))
