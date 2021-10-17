import sys
sys.stdin = open('input.txt')

S = input()
T = input()

while len(S) < len(T):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1][::-1]
result = 1 if S == T else 0

print(result)

# 숏코딩
# S, T = input(), input()
# while len(S) < len(T):
#     T = T[:-1] if T[-1] == 'A' else T[:-1][::-1]
# result = 1 if S == T else 0
# print(result)