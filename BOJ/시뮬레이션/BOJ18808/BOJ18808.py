import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


# 90도 회전
def rotate90(matrix: list) -> list:
    ans = [i[::-1] for i in zip(*matrix)]
    return ans


# 스티커 붙일 수 있는 위치인지 체크
def can_sticker(dr, dc):
    for r in range(R):
        for c in range(C):
            # 범위 넘어가면 못 붙임
            if not (0 <= r + dr < N and 0 <= c + dc < M):
                return 0
            # 노트북이랑 스티커가 겹치면 붙일 수 없음
            if notebook[r + dr][c + dc] and sticker[r][c]:
                return 0
    # 모든 곳이 겹치지 않으면 붙일 수 있음
    return 1


# 스티커 붙이기
def put_sticker(dr, dc):
    for r in range(R):
        for c in range(C):
            if sticker[r][c]:
                notebook[r + dr][c + dc] = 1
    return 1


# 스티커 붙일 자리 찾기
def find_sticker_position_and_put():
    # flag : 스티커 붙였는지
    flag = 0
    for dr in range(N - R+1):
        for dc in range(M - C+1):
            # 만약 스티커 붙일 수 있으면 스티커 붙이고 끝내기
            if can_sticker(dr, dc):
                flag = put_sticker(dr, dc)
                return flag
    return flag


N, M, K = map(int, input().split())
notebook = [[0] * M for _ in range(N)]

for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]

    # 4방향 회전하면서 위치 찾기
    for rotate_num in range(4):
        flag = find_sticker_position_and_put()
        # 스티커 붙일 수 있는 자리 찾고 붙였으면 끝
        if flag:
            break
        # 못찾았으면 회전하고 R, C 바꾸기
        else:
            sticker = rotate90(sticker)
            R, C = C, R

# 스티커가 붙은 칸의 수 출력
ans = 0
for i in range(N):
    ans += sum(notebook[i])
print(ans)
