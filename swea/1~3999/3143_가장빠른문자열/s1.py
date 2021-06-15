import sys
sys.stdin = open("input.txt", "r")

# A=”asakusa”, B=”sa”
for tc in range(1, int(input()) + 1):
    A, B = input().split()
    cnt = 0

    # [i:i+len(B)]가 A의 마지막 인덱스와 비교할때까지 [?:len(A)] 반복 따라서 i+len(B) <= len(A).
    # A 안에서 B 문자열을 찾으면 i 의 값을 +len(B)만큼 이동하고, 못찾으면 +1 만큼 이동한다
    i = 0
    while i+len(B) <= len(A):
        if A[i:i + len(B)] == B:
            cnt += 1
            i += len(B) - 1   # 다음 줄에서 +1 해주니 len(B)-1 만큼 이동
        i += 1

    # 문자열 A를 타이핑 한다고 하면 len(A) 만큼 키를 눌러야하고,
    # 한번에 B를 타이핑할때마다 len(B)-1씩 키 누르는 횟수가 줄어든다.
    print("#{} {}".format(tc, len(A) - (len(B)-1)*cnt))