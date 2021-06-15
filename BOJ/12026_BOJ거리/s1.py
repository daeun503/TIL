import sys
sys.stdin = open('input.txt')

# def my_func(idx, energy):
#     global result
#
#     if idx == N-1:
#         if result > energy:
#             result = energy
#         return
#
#     if result <= energy:
#         return
#
#     for i in range(idx+1, N):
#         if (IN[idx] == 'B' and IN[i] == 'O') or\
#             (IN[idx] == 'O' and IN[i] == 'J') or\
#             (IN[idx] == 'J' and IN[i] == 'B'):
#             my_func(i, energy + (i - idx) ** 2)
#
#
# for tc in range(int(input())):
#     N = int(input())
#     IN = input()
#     result = 9999999999999999
#     my_func(0, 0)
#     print(-1) if result == 9999999999999999 else print(result)


# DP 위는 백트래킹
N = int(input())
IN = input()

E = [99999999] * N
E[0] = 0
for idx in range(1, N):
    tmp = []
    # i에서 idx 위치로 도착하기 위한 점프 에너지 tmp
    for i in range(idx):
        if (IN[idx] == 'B' and IN[i] == 'J') or\
            (IN[idx] == 'O' and IN[i] == 'B') or\
            (IN[idx] == 'J' and IN[i] == 'O'):
            tmp.append(E[i] + (idx-i)**2)
    # E[idx]는 tmp들 중 최솟값, tmp가 비어있으면 i에서 idx로 못감
    E[idx] = min(tmp) if tmp else 99999999

print(E[N-1]) if E[N-1] < 99999999 else print(-1)



