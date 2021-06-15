
import sys
sys.stdin = open('input.txt')

# 총 N명, K를 말하는 사람 퇴장, 나는 M번째
N, K, M = map(int, input().split())

# KK는 퇴장하는 사람 위치. K가 N이상일 때 보정
KK = K % N if K % N else N
result = 0

while N != 1:
    if M == KK: break            # 퇴장하는 위치가 내 위치면 break
    result += 1                  # 퇴장하는 위치가 내 위치 아니면
    # KK 위치가 M 위치 이상이면 -KK만, 이하면 KK 이하를 다 맨 뒤로
    M = M - KK if M > KK else (N - KK) + M
    N -= 1                       # 사람 수 한 명 줄어듦
    KK = K % N if K % N else N   # N이 매번 바뀌므로 KK도 다시 계산

print(result + 1)