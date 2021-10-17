import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())
result = 0

while A < B :
    # 마지막 자리가 1이면 1 떼기
    if str(B)[-1] == '1':
        B = int(str(B)[:-1])
    # 마지막 자리가 2로 나눠지면 2나누기
    elif B % 2 == 0:
        B //= 2
    # 둘 다 아니면 X
    else: break
    result += 1

print(result+1) if A == B else print(-1)
