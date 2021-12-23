import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
S = list(map(int, input().split()))

result, length = 0, 0
s, e = 0, 0

while e < N:
    # 다음이 짝수이면 길이 +1, e 전진
    if not S[e] % 2:
        length += 1
        e += 1
        if length > result:
            result = length
        continue

    # 다음이 홀수이면
    # 삭제가 가능한 경우 : K를 줄이고 e 전진
    if K:
        K -= 1
        e += 1
        continue

    # 삭제가 불가능한 경우
    # 홀 => K를 복구시키고 s 전진 // 짝 => length 줄이고 s 전진
    while not K:
        if S[s] % 2:
            K += 1
        else:
            length -= 1
        s += 1

print(result)
