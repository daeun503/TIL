import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 동서남북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


# input 데이터 형식 지정
def attack_input(s):
    if s == "E":
        return 0
    elif s == "W":
        return 1
    elif s == "S":
        return 2
    elif s == "N":
        return 3
    else:
        return int(s)


def attack(AX, AY, AD):
    r, c, d = AX, AY, AD
    # r,c 도미노가 이미 쓰러져있으면 0점, 서있었으면 1점부터 시작
    score = 0 if status[r][c] else 1
    status[r][c] = 1

    # q에서 뽑으면서 쓰러뜨리기
    q = [(r, c, d)]
    while q:
        r, c, d = q.pop(0)
        height = IN[r][c]

        # 높이만큼 쓰러뜨리기
        for h in range(1, height):
            nr = r + dr[d] * h
            nc = c + dc[d] * h

            # 범위 바깥이면 X
            if not(0 <= nr < N and 0 <= nc < M):
                break

            # 도미노가 서 있었으면 점수 +1, 상태 쓰러진걸로 갱신, q에 추가
            if not status[nr][nc]:
                score += 1
                status[nr][nc] = 1
                q.append((nr, nc, d))

    return score


N, M, R = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]
status = [[0] * M for _ in range(N)]
attack_score = 0

# attack : A / defense : D
for _ in range(R):
    # 공격
    AX, AY, AD = map(attack_input, input().split())
    attack_score += attack(AX-1, AY-1, AD)

    # 수비
    DX, DY = map(int, input().split())
    status[DX-1][DY-1] = 0

# 출력 형식 지정
for r in range(N):
    for c in range(M):
        if status[r][c]:
            status[r][c] = "F"
        else:
            status[r][c] = "S"

print(attack_score)
for i in range(N):
    print(*status[i])
