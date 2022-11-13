import sys
from collections import Counter

# 그냥 input()으로 받으면 시간 초과
M, N = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
IN = [list(sys.stdin.readline()) for _ in range(M)]

JOI = [[Counter({"J": 0, "O": 0, "I": 0}) for _ in range(N)] for _ in range(M)]
for r in range(M):
    for c in range(N):
        area = IN[r][c]
        if r == 0 and c == 0:
            pass
        elif r == 0:
            JOI[r][c] += JOI[r][c - 1]
        elif c == 0:
            JOI[r][c] += JOI[r - 1][c]
        else:
            JOI[r][c] += JOI[r][c - 1] + JOI[r - 1][c] - JOI[r - 1][c - 1]
        JOI[r][c][area] += 1


# Counter를 이용하여 덧셈을 할 수 있다.
# 단, 진짜 개수를 세는 것이기 때문에 음수가 될 수 없다
# 그래서 r1 > 0 and c1 > 0 인 경우를 미리 더해줘서 양수가 나오게 한다
for _ in range(K):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    r1 -= 1; c1 -= 1
    r2 -= 1; c2 -= 1

    value = JOI[r2][c2].copy()
    if r1 > 0 and c1 > 0:
        value += JOI[r1 - 1][c1 - 1]
    if r1 > 0:
        value -= JOI[r1 - 1][c2]
    if c1 > 0:
        value -= JOI[r2][c1 - 1]

    print(f"{value['J']} {value['O']} {value['I']}")
